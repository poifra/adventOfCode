#![allow(dead_code)]
use crate::utils;
pub fn part1() {
    let file = utils::read_lines("day2.txt");
    let mut sum = 0;
    const MAX_RED: u32 = 12;
    const MAX_GREEN: u32 = 13;
    const MAX_BLUE: u32 = 14;
    for line in file {
        let game_id = line[5..line.find(':').unwrap()].parse::<u32>().unwrap();
        let data = line[line.find(':').unwrap() + 2..line.len()].split("; ");
        let mut valid: bool = true;
        for attempt in data {
            if !valid {
                break;
            }
            let color = attempt.split(", ");
            for c in color {
                if !valid {
                    break;
                }
                match c.find(" red") {
                    None => (),
                    Some(index) => match c[0..index].parse::<u32>() {
                        Err(oh_no) => println!("Line {game_id} died on red because {oh_no}"),
                        Ok(amount) => valid &= amount <= MAX_RED,
                    },
                };
                match c.find(" green") {
                    None => (),
                    Some(index) => match c[0..index].parse::<u32>() {
                        Err(oh_no) => println!("Line {game_id} died on green because {oh_no}"),
                        Ok(amount) => valid &= amount <= MAX_GREEN,
                    },
                };
                match c.find(" blue") {
                    None => (),
                    Some(index) => match c[0..index].parse::<u32>() {
                        Err(oh_no) => println!("Line {game_id} died on blue because {oh_no}"),
                        Ok(amount) => valid &= amount <= MAX_BLUE,
                    },
                };
            }
        }
        if valid {
            sum += game_id;
        }
    }
    println!("{sum}");
}

pub fn part2() {
    let file = utils::read_lines("day2.txt");
    let mut sum = 0;
    for line in file {
        let data = line[line.find(':').unwrap() + 2..line.len()].split("; ");
        let mut max_red = 0;
        let mut max_green = 0;
        let mut max_blue = 0;
        for attempt in data {
            let color = attempt.split(", ");
            for c in color {
                match c.find(" red") {
                    None => (),
                    Some(index) => match c[0..index].parse::<u32>() {
                        Err(oh_no) => println!("Line died on red because {oh_no}"),
                        Ok(amount) => {
                            if amount > max_red {
                                max_red = amount;
                            }
                        }
                    },
                };
                match c.find(" green") {
                    None => (),
                    Some(index) => match c[0..index].parse::<u32>() {
                        Err(oh_no) => println!("Line died on green because {oh_no}"),
                        Ok(amount) => {
                            if amount > max_green {
                                max_green = amount;
                            }
                        }
                    },
                };
                match c.find(" blue") {
                    None => (),
                    Some(index) => match c[0..index].parse::<u32>() {
                        Err(oh_no) => println!("Line died on blue because {oh_no}"),
                        Ok(amount) => {
                            if amount > max_blue {
                                max_blue = amount;
                            }
                        }
                    },
                };
            }
        }
        //let game_id = line[5..line.find(":").unwrap()].parse::<u32>().unwrap();
        //println!("Line {game_id} is possible with {max_red} red {max_green} green {max_blue} blue");
        sum += max_red * max_green * max_blue;
    }
    println!("{sum}");
}
