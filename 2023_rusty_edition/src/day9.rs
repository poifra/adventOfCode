use crate::utils;

fn calc(numbers: Vec<i32>) -> i32 {
    let deltas: Vec<i32> = numbers
        .iter()
        .zip(numbers.iter().skip(1))
        .map(|(first, second)| second - first)
        .collect();

    if deltas.iter().all(|n| *n == 0) {
        *numbers.last().unwrap()
    } else {
        calc(deltas) + numbers.last().unwrap()
    }
}

pub fn part1(flag_part_2: bool) {
    let input = utils::read_lines("day9.txt");
    println!("{0}",input
        .iter()
        .map(|line| {
            let mut numbers: Vec<i32> =
                line.split(' ').map(|s| s.parse::<i32>().unwrap()).collect();
            if flag_part_2 {
                numbers.reverse()
            }
            calc(numbers)
        })
        .sum::<i32>())
}
