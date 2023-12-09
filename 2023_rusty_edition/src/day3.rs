#![allow(dead_code)]
use crate::utils;
use regex::Regex;
use std::{cmp, collections::HashMap};

pub fn part1() {
    //  println!("{0}",(0 as usize).saturating_sub(1));
    let input = utils::read_lines("day3.txt");
    let number_finder = Regex::new(r"\d+").unwrap();
    let mut sum = 0;
    for i in 0..input.len() {
        let row = &input[i];
        for num in number_finder.find_iter(row) {
            let start: usize = num.start();
            let end: usize = num.end();
            // println!("Checking {0}",row[num.start()..num.end()].to_string());

            // check right
            if end < row.len()
                && row.as_bytes()[end] != b'.'
                && !row.as_bytes()[end].is_ascii_digit()
            {
                sum += row[num.start()..num.end()]
                    .to_string()
                    .parse::<u32>()
                    .unwrap();
                // println!(
                //     "{} is a part because of symbol on right",
                //     row[num.start()..num.end()].to_string()
                // );
            }

            // check left
            if start > 0
                && row.as_bytes()[start - 1] != b'.'
                && !row.as_bytes()[start - 1].is_ascii_digit()
            {
                sum += row[num.start()..num.end()]
                    .to_string()
                    .parse::<u32>()
                    .unwrap();
                // println!(
                //     "{} is a part because of symbol on left",
                //     row[num.start()..num.end()].to_string()
                // );
            }

            // check below
            if i + 1 < input.len() {
                let row_below = &input[i + 1];
                for c in
                    row_below[start.saturating_sub(1)..cmp::min(end + 1, row_below.len())].chars()
                {
                    if c != '.' && !c.is_ascii_digit() {
                        sum += row[num.start()..num.end()]
                            .to_string()
                            .parse::<u32>()
                            .unwrap();
                        // println!(
                        //     "{} is a part because of symbol below",
                        //     row[num.start()..num.end()].to_string()
                        // );
                    }
                }
            }

            // check above
            if i > 0 {
                let row_below = &input[i - 1];
                for c in
                    row_below[start.saturating_sub(1)..cmp::min(end + 1, row_below.len())].chars()
                {
                    if c != '.' && !c.is_ascii_digit() {
                        sum += row[num.start()..num.end()]
                            .to_string()
                            .parse::<u32>()
                            .unwrap();
                        // println!(
                        //     "{} is a part because of symbol above",
                        //     row[num.start()..num.end()].to_string()
                        // );
                    }
                }
            }
        }
    }
    println!("{sum}");
}

pub fn part2() {
    //  println!("{0}",(0 as usize).saturating_sub(1));
    let input = utils::read_lines("day3.txt");
    let number_finder = Regex::new(r"\d+").unwrap();
    let mut gears: HashMap<(usize, usize), Vec<u32>> = HashMap::new();
    let mut sum = 0;
    for i in 0..input.len() {
        let row = &input[i];
        for num in number_finder.find_iter(row) {
            let start: usize = num.start();
            let end: usize = num.end();
            // println!("Checking {0}", &row[num.start()..num.end()]);

            // check right
            if end < row.len() && row.as_bytes()[end] == b'*' {
                gears
                    .entry((i, end))
                    .or_default()
                    .push(row[start..end].to_string().parse::<u32>().unwrap());
            }

            // check left
            if start > 0 && row.as_bytes()[start - 1] == b'*' {
                gears.entry((i, start - 1)).or_default().push(
                    row[num.start()..num.end()]
                        .to_string()
                        .parse::<u32>()
                        .unwrap(),
                );
            }

            // check below
            if i + 1 < input.len() {
                let row_below = &input[i + 1];
                for j in start.saturating_sub(1)..end + 1 {
                    if j < row_below.len() && row_below.as_bytes()[j] == b'*' {
                        gears.entry((i + 1, j)).or_default().push(
                            row[num.start()..num.end()]
                                .to_string()
                                .parse::<u32>()
                                .unwrap(),
                        );
                    }
                }
            }

            // check above
            if i > 0 {
                let row_above = &input[i - 1];
                for j in start.saturating_sub(1)..end + 1 {
                    if j < row_above.len() && row_above.as_bytes()[j] == b'*' {
                        gears.entry((i - 1, j)).or_default().push(
                            row[num.start()..num.end()]
                                .to_string()
                                .parse::<u32>()
                                .unwrap(),
                        );
                    }
                }
            }
        }
    }
    for (_, v) in gears.into_iter() {
        // let joined: String = v.iter().map(|&id| id.to_string() + ",").collect();
        // println!("{0}, {1}: {2}", k.0, k.1, joined);
        if v.len() == 2 {
            sum += v[0] * v[1];
        }
    }
    println!("{sum}");
}
