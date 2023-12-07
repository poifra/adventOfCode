mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod utils;

use std::{collections::HashMap, cmp::Ordering};

use itertools::Itertools;

#[derive(Debug, Ord, PartialOrd, Eq, PartialEq, Copy, Clone)]
enum SuiteType {
    FiveOfAKind = 7,
    FourOfAKind = 6,
    FullHouse = 5,
    ThreeOfAKind = 4,
    TwoPair = 3,
    OnePair = 2,
    HighCard = 1,
}
#[derive(Debug, Eq, PartialEq, Clone)]
struct Hand {
    suite_type: SuiteType,
    bet: usize,
    cards: String,
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.suite_type != other.suite_type {
            self.suite_type.cmp(&other.suite_type)
        } else {
            let mut i = 0;
            let mut values: HashMap<char, u32> = HashMap::new();
            values.insert('A', 14);
            values.insert('K', 13);
            values.insert('Q', 12);
            values.insert('J', 11);
            values.insert('T', 10);
            values.insert('9', 9);
            values.insert('8', 8);
            values.insert('7', 7);
            values.insert('6', 6);
            values.insert('5', 5);
            values.insert('4', 4);
            values.insert('3', 3);
            values.insert('2', 2);
            while self.cards.as_bytes()[i] == other.cards.as_bytes()[i] {
                i += 1;
            }
    
            let first_value = self.cards.chars().nth(i).unwrap();
            let second_value = other.cards.chars().nth(i).unwrap();

            if values.get(&first_value).or(None) > values.get(&second_value).or(None) {
                Ordering::Greater
            } else {
                Ordering::Less
            }
        }
    }
}

fn main() {
    part1();
}

pub fn part1() {
    let input = utils::read_lines("day7.txt");
    let mut hands: Vec<Hand> = Vec::new();
    for line in input {
        if let Some((card, bet)) = line.split_once(' ') {
            let s = Hand {
                suite_type: get_suite_type(card.to_string()),
                bet: bet.parse::<usize>().unwrap(),
                cards: card.to_string(),
            };
            hands.push(s);
        }
    }

    hands.sort();
    for h in hands.clone() {
        println!("{:?}", h);
    }
    let mut sum = 0;
    for (i,h) in hands.iter().enumerate(){
        sum += h.bet*(i+1);
    }

    println!("{sum}");
}

fn get_suite_type(cards: String) -> SuiteType {
    let count_letters: HashMap<char, u32> = cards
        .chars()
        .into_group_map_by(|&letter| letter)
        .into_iter()
        .map(|(k, v)| (k, v.len() as u32))
        .collect();
    let num_of_5s = count_letters
        .clone()
        .into_iter()
        .filter(|(_, v)| *v == 5)
        .count();
    let num_of_4s = count_letters
        .clone()
        .into_iter()
        .filter(|(_, v)| *v == 4)
        .count();
    let num_of_3s = count_letters
        .clone()
        .into_iter()
        .filter(|(_, v)| *v == 3)
        .count();
    let num_of_2s = count_letters
        .clone()
        .into_iter()
        .filter(|(_, v)| *v == 2)
        .count();

    match (num_of_2s, num_of_3s, num_of_4s, num_of_5s) {
        (0, 0, 0, 1) => SuiteType::FiveOfAKind,
        (0, 0, 1, 0) => SuiteType::FourOfAKind,
        (1, 1, 0, 0) => SuiteType::FullHouse,
        (0, 1, 0, 0) => SuiteType::ThreeOfAKind,
        (2, 0, 0, 0) => SuiteType::TwoPair,
        (1, 0, 0, 0) => SuiteType::OnePair,
        _ => SuiteType::HighCard,
    }
}
