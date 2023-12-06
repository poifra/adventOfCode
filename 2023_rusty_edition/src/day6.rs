pub fn part1(flag_part_2: bool) {
    match flag_part_2 {
        true => {
            let time: u64 = 44899691;
            let distance: u64 = 277113618901768;
            //test input
            // let time:u64 = 71530;
            // let distance:u64 = 277113618901768;
            println!(
                "{0}",
                (0..time).filter(|&t| t * (time - t) > distance).count() as u64
            );
        }
        false => {
            let times: Vec<u32> = vec![44, 89, 96, 91];
            let distances: Vec<u32> = vec![277, 1136, 1890, 1768];
            println!(
                "{0}",
                times
                    .iter()
                    .zip(distances.iter())
                    .map(|(time, distance)| (0..*time)
                        .filter(|&i| i * (time - i) > *distance)
                        .count())
                    .product::<usize>()
            );
        }
    };
}
