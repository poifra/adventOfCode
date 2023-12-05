use crate::utils;

use std::collections::HashMap;

pub fn part1() {
    let input = utils::read_lines("day4.txt");
    let mut sum = 0;
    for line in input {
        let mut card_value = 1;
        let start = line.find(':').unwrap();
        let card_numbers: Vec<String> = line[start + 1..line.find('|').unwrap()]
            .trim()
            .replace("  ", " ")
            .split(' ')
            .map(|s| s.to_string())
            .collect();
        let winning_numbers: Vec<String> = line[line.find('|').unwrap() + 1..line.len()]
            .trim()
            .replace("  ", " ")
            .split(' ')
            .map(|s| s.to_string())
            .collect();
        for card_num in card_numbers {
            if winning_numbers.contains(&card_num) {
                card_value *= 2;
            }
        }

        sum += card_value >> 1; // 1 will be 0, meaning we found no match
    }
    println!("{sum}");
}

pub fn part2() {
    let input = utils::read_lines("day4.txt");
    let card_count = input.len();
    let mut yo_dawg_i_heard_you_like_cards: HashMap<usize, u32> = HashMap::new();
    for i in 1..card_count + 1 {
        //everything is processed at least once
        yo_dawg_i_heard_you_like_cards.insert(i, 1);
    }

    for line in input {
        let start = line.find(':').unwrap();
        let card_id: usize = line[5..start].trim().parse::<usize>().unwrap();
        let card_numbers: Vec<String> = line[start + 1..line.find('|').unwrap()]
            .trim()
            .replace("  ", " ")
            .split(' ')
            .map(|s| s.to_string())
            .collect();
        let winning_numbers: Vec<String> = line[line.find('|').unwrap() + 1..line.len()]
            .trim()
            .replace("  ", " ")
            .split(' ')
            .map(|s| s.to_string())
            .collect();
        for _ in 0..*yo_dawg_i_heard_you_like_cards
            .get_key_value(&card_id)
            .unwrap()
            .1
        {
            let mut nth_match: usize = 1;
            for num in &card_numbers {
                if winning_numbers.contains(num) {
                    yo_dawg_i_heard_you_like_cards
                        .entry(card_id + nth_match)
                        .and_modify(|e| *e += 1);
                    nth_match += 1;
                }
            }
        }
    }
    // for (k, v) in yo_dawg_i_heard_you_like_cards.iter() {
    //     println!("card {k} has {v} copies");
    // }
    println!("{0}", yo_dawg_i_heard_you_like_cards.values().sum::<u32>());
}
