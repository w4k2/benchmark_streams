import helper as h
import strlearn as sl
import matplotlib.pyplot as plt

"""
0. Common parameters
7 attributes
2 classes
"""
length = 100000
path = "datasets/%s"
generators = {
    "s_hyp_r1": "generators.HyperplaneGenerator -a 7 -i 1 -n 5",
    "s_hyp_r2": "generators.HyperplaneGenerator -a 7 -i 2 -n 10",
    "s_hyp_r3": "generators.HyperplaneGenerator -a 7 -i 3 -n 15",
    "s_led_r1": "generators.LEDGenerator -i 1 -n 5",
    "s_led_r2": "generators.LEDGenerator -i 2 -n 10",
    "s_led_r3": "generators.LEDGenerator -i 3 -n 15",
    "s_rbf_r1": "generators.RandomRBFGenerator -n 25 -a 7 -r 1 -i 1",
    "s_rbf_r2": "generators.RandomRBFGenerator -n 50 -a 7 -r 2 -i 2",
    "s_rbf_r3": "generators.RandomRBFGenerator -n 100 -a 7 -r 3 -i 3"
}
drift_pairs = [
    ["s_hyp_r1","s_hyp_r2"], ["s_hyp_r2","s_hyp_r3"], ["s_hyp_r1","s_hyp_r3"],
    ["s_led_r1","s_led_r2"], ["s_led_r2","s_led_r3"], ["s_led_r1","s_led_r3"],
    ["s_rbf_r1","s_rbf_r2"], ["s_rbf_r2","s_rbf_r3"], ["s_rbf_r1","s_rbf_r3"],
    ["s_hyp_r1","s_rbf_r1"], ["s_hyp_r2","s_rbf_r2"], ["s_hyp_r3","s_rbf_r3"]
]

def test(dbname):
    X, y = sl.utils.load_arff(path % "%s.arff" % dbname )
    learner = sl.Learner(X,y,chunk_size=100,evaluate_interval=1000)
    learner.run()
    print(learner.scores)
    plt.plot(learner.score_points,learner.scores)
    plt.title(dbname)
    plt.ylim([0,1])
    plt.savefig("figures/%s.png" % dbname)
    plt.clf()

"""
1. Stationary streams
"""
window = 0
for key in generators:
    generator = generators[key]
    print(generator, key)
    h.generate_stream(path % key, length, window, [generator])
    test(key)

"""
2. Sudden drifts
"""
window = 0
for drift_pair in drift_pairs:
    first, second = drift_pair
    g_first, g_second = generators[first], generators[second]
    streams = [g_first, g_second, g_first, g_second, g_first]
    filename = "sd_%s_%s" % (first, second)
    print(filename)
    h.generate_stream(path % filename, length, window, streams)
    test(filename)

"""
3. Incremental drifts
"""
window = length / 4
for drift_pair in drift_pairs:
    first, second = drift_pair
    g_first, g_second = generators[first], generators[second]
    streams = [g_first, g_second, g_first, g_second, g_first]
    filename = "id_%s_%s" % (first, second)
    print(filename)
    h.generate_stream(path % filename, length, window, streams)
    test(filename)
    
