fn main() {
    let mut c = 0;
    for i in 765_432_015..=1_542_613_239 {
        let k = f(i);
        let p = f(i+1);
        if k > p{
            c += 1
        }
    }
    println!("{c}")
}


fn f(n: u64) -> u64 {
    if n == 0 {
        return 0;
    }
    return f(n / 10) + (n % 10)
}
