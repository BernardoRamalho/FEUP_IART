from gym.envs.registration import register

register(
    id='pivit-v0',
    entry_point='gym_pivit.envs:PivitEnv',
)
register(
    id='pivit-extrahard-v0',
    entry_point='gym_pivit.envs:PivitExtraHardEnv',
)
