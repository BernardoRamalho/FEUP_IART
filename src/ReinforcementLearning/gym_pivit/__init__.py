from gym.envs.registration import register

register(
    id='pivit-v0',
    entry_point='gym_pivit.envs:PivitEnv',
)
