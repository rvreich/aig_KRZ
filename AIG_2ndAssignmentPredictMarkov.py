import numpy as np
from hmmlearn import hmm

states = ["MU Win","Liverpool Win"]
n_states = len(states)

observations = ["Win","Draw","Lose"]
n_observations = len(observations)

model = hmm.MultinomialHMM(n_components=n_states, init_params="")
model.startprob_ = np.array([0.5 , 0.5])
model.transmat_ = np.array([
    [0.6, 0.4],
    [0.3, 0.7]
])
model.emissionprob_ = np.array([
    [0.9, 0.1],
    [0.2, 0.8]
])

# predict a sequence of states
outcome = np.array([[1, 1, 1, 0, 0]]).T

model = model.fit(outcome)
logprob, final = model.decode(outcome,algorithm="viterbi")
print("Sequence: ", ", ".join(map(lambda x: states[x], final)))
print(logprob)