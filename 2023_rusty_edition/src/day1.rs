#![allow(dead_code)]
use crate::utils;
pub fn part1(replace_words: bool) {
    let path = "day1.txt";
    let result = utils::read_lines(path);
    let mut sum = 0;
    for mut line in result {
        if replace_words {
            // there can be overlap, like oneight
            line = line.replace("one", "o1e");
            line = line.replace("two", "t2o");
            line = line.replace("three", "t3e");
            line = line.replace("four", "f4r");
            line = line.replace("five", "f5e");
            line = line.replace("six", "s6x");
            line = line.replace("seven", "s7n");
            line = line.replace("eight", "e8t");
            line = line.replace("nine", "n9e");
        }
        let rev_string = line.chars().rev();
        let mut num1: char = char::default();
        let mut num2: char = char::default();
        for c in line.chars() {
            if c.is_ascii_digit() {
                num1 = c;
                break;
            }
        }
        for c in rev_string {
            if c.is_ascii_digit() {
                num2 = c;
                break;
            }
        }
        let number = format!("{num1}{num2}").parse::<i32>().unwrap();
        sum += number;
        // println!("Found {number}")
    }
    println!("{sum}");
}

pub fn part2() {
    part1(true)
}
