use crate::utils;
use rayon::prelude::*;

struct Mapping {
    start: u64,
    end: u64,
    range: u64,
}

enum CurrentMapping {
    SeedToSoil = 1,
    SoilToFertilizer = 2,
    FertilizerToWater = 3,
    WaterToLight = 4,
    LightToTemperature = 5,
    TemperatureToHumidity = 6,
    HumidityToLocation = 7,
}
pub fn part1(part_2_flag: bool) {
    let input = utils::read_lines("day5.txt");
    let mut mapping = CurrentMapping::SeedToSoil;
    let mut seeds: Vec<u64> = Vec::new();

    let mut seed_to_soil: Vec<Mapping> = Vec::new();
    let mut soil_to_fertilizer: Vec<Mapping> = Vec::new();
    let mut fertilizer_to_water: Vec<Mapping> = Vec::new();
    let mut water_to_light: Vec<Mapping> = Vec::new();
    let mut light_to_temperature: Vec<Mapping> = Vec::new();
    let mut temperature_to_humidity: Vec<Mapping> = Vec::new();
    let mut humidity_to_location: Vec<Mapping> = Vec::new();

    for line in input {
        //   println!("{line}");
        if line.is_empty() {
            continue;
        }
        if line.starts_with("seeds:") {
            seeds = line[7..]
                .split(' ')
                .map(|s| s.parse::<u64>().unwrap())
                .collect();
            continue;
        }

        if line.find('-').is_none() {
            match mapping {
                CurrentMapping::SeedToSoil => fill_map2(&line, &mut seed_to_soil),
                CurrentMapping::SoilToFertilizer => fill_map2(&line, &mut soil_to_fertilizer),
                CurrentMapping::FertilizerToWater => fill_map2(&line, &mut fertilizer_to_water),
                CurrentMapping::WaterToLight => fill_map2(&line, &mut water_to_light),
                CurrentMapping::LightToTemperature => fill_map2(&line, &mut light_to_temperature),
                CurrentMapping::TemperatureToHumidity => {
                    fill_map2(&line, &mut temperature_to_humidity)
                }
                CurrentMapping::HumidityToLocation => fill_map2(&line, &mut humidity_to_location),
            }
            continue;
        }

        match &line[0..line.find('-').unwrap()] {
            "seed" => {
                mapping = CurrentMapping::SeedToSoil;
                continue;
            }
            "soil" => {
                mapping = CurrentMapping::SoilToFertilizer;
                continue;
            }
            "fertilizer" => {
                mapping = CurrentMapping::FertilizerToWater;
                continue;
            }
            "water" => {
                mapping = CurrentMapping::WaterToLight;
                continue;
            }
            "light" => {
                mapping = CurrentMapping::LightToTemperature;
                continue;
            }
            "temperature" => {
                mapping = CurrentMapping::TemperatureToHumidity;
                continue;
            }
            "humidity" => {
                mapping = CurrentMapping::HumidityToLocation;
                continue;
            }
            _ => (),
        }
    }

    let mut min_loc: u64 = u64::MAX;

    if part_2_flag {
        let real_seeds: Vec<u64> = seeds.iter().step_by(2).map(|e| *e).collect();
        let seed_range: Vec<u64> = seeds.iter().skip(1).step_by(2).map(|e| *e).collect();

        // Use Rayon's par_iter() to parallelize the loop and reduce to find the minimum
        min_loc = real_seeds
            .par_iter()
            .enumerate()
            .map(|(index, seed)| {
                let range = seed_range[index];
                (0..range)
                    .into_par_iter()
                    .map(|num| {
                        let current_seed = seed + num;
                        let soil = mapper(&seed_to_soil, current_seed);
                        let fertilizer = mapper(&soil_to_fertilizer, soil);
                        let water = mapper(&fertilizer_to_water, fertilizer);
                        let light = mapper(&water_to_light, water);
                        let temperature = mapper(&light_to_temperature, light);
                        let humidity = mapper(&temperature_to_humidity, temperature);
                        let location = mapper(&humidity_to_location, humidity);
                        location
                    })
                    .reduce(|| u64::MAX, |a, b| if a < b { a } else { b })
            })
            .reduce(|| u64::MAX, |a, b| if a < b { a } else { b });
    } else {
        // Use Rayon's par_iter() to parallelize the loop and reduce to find the minimum
        min_loc = seeds
            .par_iter()
            .map(|&num| {
                let soil = mapper(&seed_to_soil, num);
                let fertilizer = mapper(&soil_to_fertilizer, soil);
                let water = mapper(&fertilizer_to_water, fertilizer);
                let light = mapper(&water_to_light, water);
                let temperature = mapper(&light_to_temperature, light);
                let humidity = mapper(&temperature_to_humidity, temperature);
                let location = mapper(&humidity_to_location, humidity);
                location
            })
            .reduce(|| u64::MAX, |a, b| if a < b { a } else { b });
    }

    if part_2_flag {
        println!("{0}", min_loc - 1);
    } else {
        println!("{0}", min_loc);
    }
}

fn fill_map2(line: &str, map_to_fill: &mut Vec<Mapping>) {
    let nums: Vec<u64> = line.split(' ').map(|s| s.parse::<u64>().unwrap()).collect();
    let start = nums[1];
    let end = nums[0];
    let range = nums[2];
    map_to_fill.push(Mapping { start, end, range });
}

fn mapper(values: &[Mapping], seed: u64) -> u64 {
    values
        .iter()
        .find(|map| seed >= map.start && seed <= map.start + map.range)
        .map_or(seed, |map| {
            if map.start > map.end {
                seed - (map.start - map.end)
            } else {
                seed + (map.end - map.start)
            }
        })
}
