from hashlib import md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512
from time import perf_counter
from os import urandom
from matplotlib import pyplot as plt


ITERATIONS = 10


def generate_hashes_performance_test(input_data):  # zwraca listę czasów wykonania dla każdej funkcji skrótu
    hashes = [md5(), sha1(), sha224(), sha256(), sha384(), sha512(), sha3_224(), sha3_256(), sha3_384(), sha3_512()]
    times = []
    for elem in hashes:  # uruchom każdy hash na tych samych danych i zapisz czas działania
        t0 = perf_counter()
        elem.update(input_data)
        elem.hexdigest()
        t1 = perf_counter()
        times.append((t1-t0)*1000)
    return times


# rozmiary bitowe danych, dla których testujemy
# rozmiar 512 jest odrzucany; python ma tendencję do spowalniania przy pierwszym wykonywaniu obliczeń
sizes = [512] + [int(round((2**27)*x/10, -5)) for x in range(1, 11)]
scores = [[] for _ in range(10)]
for size in sizes:  # dla każdego rozmiaru danych
    temp_scores = [0 for _ in range(10)]  # suma czasów wykonania dla rozmiaru
    for _ in range(ITERATIONS):  # wykonaj wiele iteracji i uśrednij wyniki
        data = urandom(size)  # wygeneruj losowe dane o zadanej długości
        ret = generate_hashes_performance_test(data)  # przekaż dane do funkcji wyznaczającej czas
        for i in range(len(ret)):
            temp_scores[i] += (ret[i])  # sumuj czasy z każdej iteracji
    for i in range(len(temp_scores)):
        scores[i].append(temp_scores[i]/ITERATIONS)  # dodaj do wyników średni czas każdego algorytmu
scores = [x[1:] for x in scores] # odetnij rozmiar 512 z wyników
sizes = sizes[1:]  # odetnij rozmiar 512 z listy testowanych rozmiarów

# definicje dla formatowania wykresów
labels = ['MD5', 'SHA1', 'SHA2 224', 'SHA2 256', 'SHA2 384', 'SHA2 512', 'SHA3 224', 'SHA3 256', 'SHA3 384', 'SHA3 512']
formats = {
    'MD5': {'color': '#00FFFF',
            'linestyle': 'solid',
            'marker': '*'},
    'SHA1': {'color': '#FF00FF',
             'linestyle': 'solid',
             'marker': '*'},
    'SHA2 224': {'color': '#FFAAAA',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA2 256': {'color': '#FF6666',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA2 384': {'color': '#FF0000',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA2 512': {'color': '#880000',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA3 224': {'color': '#AAAAFF',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA3 256': {'color': '#6666FF',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA3 384': {'color': '#0000FF',
                 'linestyle': 'solid',
                 'marker': '*'},
    'SHA3 512': {'color': '#000088',
                 'linestyle': 'solid',
                 'marker': '*'}
}

# generowanie i formatowanie wykresu
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plots = (ax1, ax1, ax2, ax2, ax2, ax2, ax3, ax3, ax3, ax3)
for subplt, times, label in zip(plots, scores, labels):
    subplt.plot(sizes, times, label=label, color=formats[label]['color'], linestyle=formats[label]['linestyle'],
                marker=formats[label]['marker'])
    ax4.plot(sizes, times, color=formats[label]['color'], linestyle=formats[label]['linestyle'],
             marker=formats[label]['marker'])


max_times = [max([max(x) for x in scores[:2]]),
             max([max(x) for x in scores[2:6]]),
             max([max(x) for x in scores[6:]]),
             max([max(x) for x in scores])]
for subplt, max_time in zip((ax1, ax2, ax3, ax4), max_times):
    if subplt is not ax4:
        subplt.legend()
    subplt.set_xlim([0, sizes[-1]])
    subplt.set_ylim([0, max_time])
    subplt.set_xticks(sizes, [f'{x/(10**6):.2f}' for x in sizes], rotation=45)
    subplt.grid()
fig.text(0.5, 0.01, 'Rozmiar danych (w milionach bitów)', ha='center', size=20)
fig.text(0.01, 0.5, 'Czas wykonania (w sekundach)', va='center', rotation='vertical', size=20)
fig.text(0.5, 0.99, 'Czas wykonania funkcji skrótów względem rozmiaru danych', ha='center', va='top')
fig.tight_layout()
plt.show()
