use std::fs;

fn main() 
{
 //   part1(false);
    part1(true);
}
fn part1(replaceWords:bool)
{
    let path = "day1.txt";
    let result = read_lines(path);
    let mut sum = 0;
    for mut line in result
    {
        if replaceWords
        {
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
        let mut num1:char = char::default();
        let mut num2:char = char::default();
        for c in line.chars()
        {
            if c.is_digit(10)
            {
                num1 = c;
                break;
            }
        }
        for c in rev_string
        {
            if c.is_digit(10)
            {
                num2 = c;
                break;
            }
        }
        let found = format!("{num1}{num2}").parse::<i32>().unwrap();
        sum += found;
       // println!("Found {found}")
    }
    println!("{sum}");
}

fn read_lines(filename: &str) -> Vec<String> 
{
    return fs::read_to_string(filename) 
        .unwrap() 
        .lines()  
        .map(String::from) 
        .collect();
}