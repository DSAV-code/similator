// Copyright 2024 Diego San Andrés Vasco
/*
This file is part of Similator.

Similator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Similator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Similator. If not, see <https://www.gnu.org/licenses/>.
*/


use pyo3::prelude::*;
use pyo3::types::{PyList, PyTuple, PyString, PyFloat};
use std::collections::HashSet;

/// Function to search valid data and return matches above a similarity threshold.
/// 
/// # Arguments
/// * `job_str` - The reference string to compare against.
/// * `valid_data` - A vector of strings to search for similarity.
/// * `threshold` - A float value representing the minimum similarity score required to consider a match.
///
/// # Returns
/// A Python list of tuples, each containing a string from valid_data and its similarity score.
#[pyfunction]
fn rst_search(job_str: &str, valid_data: Vec<String>, threshold: f32) -> PyResult<Py<PyList>> {
    Python::with_gil(|py| {
        let mut results = Vec::new();
        for value in &valid_data {
            let score = rst_compare(job_str, &value.to_string())?;
            if score >= threshold {
                let text = PyString::new(py, &value.to_string()).to_object(py);
                let score = PyFloat::new(py, score as f64).to_object(py);
                let tuple = PyTuple::new(py, &[text, score]);
                //let tuple = PyTuple::new(py, &[text, score]);
                results.push(tuple);
            }
        }
        // Ordenar los resultados por la puntuación (de mayor a menor)
        results.sort_by(|a, b| {
            let score_a = a[1].extract().unwrap_or(0.0);
            let score_b = b[1].extract().unwrap_or(0.0);
            score_b.partial_cmp(&score_a).unwrap_or(std::cmp::Ordering::Equal)
        });
        
        Ok(PyList::new(py, &results).into())
    })
}

/// Function to compare two strings and calculate a similarity score.
/// 
/// # Arguments
/// * `job_str` - The reference string to compare.
/// * `val_str` - The string to compare against the reference string.
/// 
/// # Returns
/// A float value representing the similarity score.
#[pyfunction]
fn rst_compare(job_str: &str, val_str: &str) -> PyResult<f32> {
    let mut job_str = job_str.to_string();
    let val_str = val_str.to_string();
    let org_size: usize = job_str.chars().count();
    let val_length: usize = val_str.chars().count();
    let mut window_size: usize = val_length.min(org_size);
    let mut coincidences: f32 = 0.0;
    let mut plus: f32 = 0.0;

    'outer: loop {
        let windows_val: HashSet<&str> = __sliding_window(&val_str, window_size).collect();

        for texto in &windows_val {
            while let Some(encontrado) = job_str.find(texto) {
                job_str.drain(encontrado..encontrado + texto.len());
                coincidences += window_size as f32;

                if let Some(_) = window_size.checked_pow(2) {
                    plus += window_size.pow(2) as f32;
                }

                if coincidences == val_length as f32 || job_str.is_empty() {
                    break 'outer;
                }
            }
        }

        if window_size <= 2 {
            break 'outer;
        } else {
            window_size -= 1;
        }
    }
    Ok(__calculate_score(coincidences, plus, val_length, org_size, &job_str)?)
}

/// Function to calculate the final similarity score based on matches and discrepancies.
/// 
/// # Arguments
/// * `coincidences` - Total length of matching substrings.
/// * `plus` - Additional score based on larger matches.
/// * `val_length` - Length of the value string.
/// * `org_size` - Original size of the job string.
/// * `job_str` - The remaining part of the job string after matches have been removed.
///
/// # Returns
/// A float value representing the final similarity score.
fn __calculate_score(coincidences: f32, plus: f32, val_length: usize, org_size: usize, job_str: &str) -> PyResult<f32> {
    let discrepancies: f32 = val_length as f32 - coincidences + job_str.chars().count() as f32;
    let final_score: f32 = ((coincidences + plus / org_size as f32) - (discrepancies / val_length.min(org_size) as f32))
        / val_length.min(org_size) as f32;
    Ok(final_score.max(0.0))
}

/// Helper function to generate sliding windows of a given size from a source string.
/// 
/// # Arguments
/// * `src` - The source string to generate windows from.
/// * `win_size` - The size of the sliding window.
///
/// # Returns
/// An iterator over substrings of the source string.
fn __sliding_window<'a>(src: &'a str, win_size: usize) -> impl Iterator<Item = &'a str> + 'a {
    src.char_indices()
        .filter_map(move |(from, _)| {
            let remaining_length = src.len() - from;
            if remaining_length < win_size {
                return None;
            }
            let mut iter = src[from..].char_indices();
            iter.nth(win_size - 1).and_then(|(to, _)| {
                let end = from + to + src[from..].chars().nth(win_size - 1).unwrap().len_utf8();
                if end <= src.len() {
                    Some(&src[from..end])
                } else {
                    None
                }
            })
        })
}

/// Python module initialization for _rst_similator.
#[pymodule]
fn _rst_similator(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rst_compare, m)?)?;
    m.add_function(wrap_pyfunction!(rst_search, m)?)?;
    Ok(())
}