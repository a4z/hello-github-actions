import os
from sys import stderr

gh_action_env = os.environ.get('GITHUB_ENV', 'n/a')


with open(gh_action_env, 'a') as f:
    f.write(f"a_val=VALUE-A\n")
    f.write(f"b_val=VALUE-B\n")
