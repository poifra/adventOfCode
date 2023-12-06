pub fn part1(flag_part_2: bool) {
    if flag_part_2 {
        let time:u64 = 44899691;
        let distance:u64 = 277113618901768;
        let mut waysToWin:u64 = 0;
        //test input
        // let time:u64 = 71530;
        // let distance:u64 = 277113618901768;
        for i in 0..time {
            if i * (time - i) > distance {
                waysToWin += 1;
            }
        }
        println!("{0}",waysToWin);
    } else {
        let times: Vec<u32> = vec![44, 89, 96, 91];
        let distances: Vec<u32> = vec![277, 1136, 1890, 1768];
        //test input
        // let times: Vec<u32> = vec![7, 15, 30];
        // let distances: Vec<u32> = vec![9, 40, 200];
        let mut waysToWin: Vec<u32> = vec![0; times.len()];
        for (index, time) in times.iter().enumerate() {
            for i in 0..*time {
                if i * (time - i) > distances[index] {
                    waysToWin[index] += 1;
                }
            }
        }
        println!("{0}", waysToWin.iter().product::<u32>())
    }
}
