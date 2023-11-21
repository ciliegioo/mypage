import os
import numpy as np
import collections
import math

# One Time Pad 암호화 함수
def one_time_pad_encrypt(message, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key))

# 엔트로피 계산 함수
def calculate_entropy(text):
    # 문자 빈도 계산
    frequency = collections.Counter(text)
    text_length = len(text)
    probabilities = [count/text_length for count in frequency.values()]

    # 엔트로피 계산
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy
    
def calculate_distribution(text):
    # 문자 빈도 계산
    frequency = collections.Counter(text)
    text_length = len(text)

    # 확률 분포 계산
    distribution = {char: count/text_length for char, count in frequency.items()}
    return distribution

# 메시지의 길이와 시뮬레이션 횟수 설정
message_length = 100
num_simulations = 1000

# 몬테카를로 시뮬레이션 함수
def simulate_one_time_pad(message_length, num_simulations):
    entropies = []
    distributions = []
    for _ in range(num_simulations):
        message = os.urandom(message_length)
        key = os.urandom(message_length)
        message = ''.join(chr(b % 128) for b in message)
        key = ''.join(chr(b % 128) for b in key)
        ciphertext = one_time_pad_encrypt(message, key)
        entropy = calculate_entropy(ciphertext)
        distribution = calculate_distribution(ciphertext)
        entropies.append(entropy)
        distributions.append(distribution)
    return entropies, distributions

# 몬테카를로 시뮬레이션 실행하고 결과 출력
entropies, distributions = simulate_one_time_pad(message_length, num_simulations)
print(f'엔트로피: {entropies}')
print(f'분포: {distributions}')
