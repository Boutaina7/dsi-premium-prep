
def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i, j, k, l]
                    decimal += 1

    return bin_dct

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')



def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2
    
    return bin_list[::-1]

# print(dec_to_bin(43))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)
    
    return bins_d

# for dec, bin_ in get_binary(n_bits=64).items():
#     print(f'{dec}: {bin_}')


def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, bin_ in bin_dict.items():
        sum_bits = sum(bin_)
        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1
    
    return binomial_dict


# d = binomial_distr(n_trials=8)

# for k, v in d.items():
#     print(f'{k}: {v}' )


# for k, v in d.items():
#     print(f'{k}: {round(v / sum(d.values()), 5)}' )


from random import choice

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst

def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1
    return d

# d = binary_sampling_dict(num_bits=8, num_samples=1000)

# for k, cnt in sorted(d.items()):
#     print(f'{k}: {cnt / sum(d.values())}')

# d2 = binary_sampling_dict(num_bits=8, num_samples=100)

# for k, cnt in sorted(d2.items()):
#     print(f'{k}: {cnt / sum(d2.values())}')


def binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

# d = binary_sampling_clt(n_bits=8, num_samples=1000, num_sample_trials=500)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

# for k, v in sorted(d.items()):
#     print(f'{k}: {v / sum(d.values())}')


from random import random

# print(random())

def get_success(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

def generate_n_successes(n=8, p=0.5):
    return [get_success(p) for _ in range(n)]

# print(generate_n_successes(n=8, p=0.8))


def binary_sampling_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_successes(num_bits, p)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1
    return d


# d = binary_sampling_vary_p(num_bits=8, p=0.95, num_samples=1000)

# for k, cnt in sorted(d.items()):
#     print(f'{k}: {cnt / sum(d.values())}')


def binary_sampling_clt_vary_p(n_bits=8, p=0.5, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_vary_p(n_bits, p, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

# d = binary_sampling_clt_vary_p(n_bits=8, p=0.3, num_samples=1000, num_sample_trials=500)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

# for k, v in sorted(d.items()):
#     print(f'{k}: {v / sum(d.values())}')



from math import factorial   

def combinations(n, k): 
    return int(factorial(n) / (factorial(n-k) * factorial(k))) 

def binomial_pmf(n, p, k):
    return combinations(n, k) * p**k * (1-p)**(n-k)


# n, k, p = 12, 7, 0.5

# print(binomial_pmf(n, p, k))


n, k, p = 12, 4, 0.3

# print(binomial_pmf(n, p, k))

n, k, p = 14, 6, 0.4

# print(binomial_pmf(n, p, k))


def binomial_cdf(n, k_high, p=0.5):
    res = []

    for i in range(k_high+1):
        res.append(binomial_pmf(n, p, k_high))

    return sum(res)
