refresh_data_flag=False

kaggle_cmd = 'kaggle datasets download -d kendallgillies/video-game-sales-and-ratings'
repo_path='..'
raw_data_path = repo_path+'/data/raw_data/'
zip_file_path = raw_data_path+'video-game-sales-and-ratings.zip'
zip_extract_path = raw_data_path+'video-game-sales-and-ratings/'
csv_fpath = zip_extract_path+'Video_Game_Sales_as_of_Jan_2017.csv'

train_frac = 0.75

sample_size=1000

njobs = 4

hier_stan_code = """
    data {
        int<lower=0> J;
        int<lower=0> N;
        int hier[N];
        vector[N] x;
        vector[N] y;
    }
    parameters {
        vector[J] a;
        vector[J] b;
        real mu_a;
        real<lower=0> sigma_a;
        real mu_b;
        real<lower=0> sigma_b;
        real<lower=0> sigma_y;
    }
    model {
        mu_a ~ normal (0,1);
        sigma_a ~ cauchy(0,1);
        a ~ normal (mu_a, sigma_a);
        
        mu_b ~ normal(0,1);
        sigma_b ~ cauchy(0,1);
        b ~ normal (mu_b, sigma_b);
        
        sigma_y ~ cauchy(0,1);
        y ~ normal(a[hier] + b[hier].*x, sigma_y);
    }
    """
