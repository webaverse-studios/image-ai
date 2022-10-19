import git
import os
import wget

# AUTOMATIC1111 git constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INVOKEAI_REPO = 'https://github.com/invoke-ai/InvokeAI.git'
INVOKEAI_LOCAL_PATH = os.path.join(ROOT_DIR, 'InvokeAI')
INVOKEAI_COMMIT_ID = '90d37eac034592cc3aed5a15a98971801b21988e'

# Switch to InvokeAI commit
repo = git.Repo.clone_from(INVOKEAI_REPO, INVOKEAI_LOCAL_PATH, no_checkout=True)
repo.git.checkout(INVOKEAI_COMMIT_ID)


