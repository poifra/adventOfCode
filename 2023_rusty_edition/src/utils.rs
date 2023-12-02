use std::fs;
pub fn read_lines(filename: &str) -> Vec<String> {
    return fs::read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect();
}
