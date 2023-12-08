use itertools::Itertools;

use crate::utils;
use std::collections::HashMap;

fn lcm(first: u64, second: u64) -> u64 {
    first * second / gcd(first, second)
}

fn gcd(first: u64, second: u64) -> u64 {
    let mut max = first;
    let mut min = second;
    if min > max {
        let val = max;
        max = min;
        min = val;
    }

    loop {
        let res = max % min;
        if res == 0 {
            return min;
        }

        max = min;
        min = res;
    }
}

pub fn part1(part_2_flag: bool) {
    let input = utils::read_lines("day8.txt");
    let mut node_mapping: HashMap<(String, char), String> = HashMap::new();
    let mut directions: String = String::new();
    let mut current_node: String = String::new();

    for mut line in input {
        if line.is_empty() {
            continue;
        }

        if (line.starts_with('R') || line.starts_with('L')) && !line.contains('=') {
            directions = line;
        } else {
            line = line
                .replace('(', "")
                .replace(')', "")
                .replace(" =", "")
                .replace(',', "")
                .trim()
                .to_string();
            //println!("{line}");

            let mut split = line.split(' ').map(String::from).into_iter();

            let node = split.next().unwrap();
            let left = split.next().unwrap();
            let right = split.next().unwrap();

            node_mapping.insert((node.clone(), 'L'), left);
            node_mapping.insert((node.clone(), 'R'), right);
        }
    }

    if part_2_flag {
        let lcm = node_mapping
            .keys()
            .filter(|(n, _)| n.ends_with('A'))
            .map(|(n, _)| n.to_string())
            .unique()
            .map(|mut p| {
                let mut steps = 0;
                while !p.ends_with('Z') {
                    p = node_mapping[&(
                        p.clone(),
                        (directions.chars().nth(steps % directions.len()).unwrap()),
                    )]
                        .clone();
                    steps += 1;
                }
                steps as u64
            })
            .into_iter()
            .reduce(|acc, n| lcm(acc, n))
            .unwrap();
        println!("{lcm}");
    } else {
        let mut steps = 0;
        current_node = "AAA".to_string();
        while current_node != "ZZZ" {
            current_node = node_mapping[&(
                current_node,
                (directions.chars().nth(steps % directions.len()).unwrap()),
            )]
                .clone();
            steps += 1;
        }
        println!("{steps}");
    }
    //println!("{:?}",node_mapping);
}
