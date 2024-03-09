# Formliss Branch Names

* Formliss follows a unified branch naming process across all of our repos. It is as follows:
  * `main` - The main branch of the project. This is where production-ready stable release can be found. If you're interested in using the latest tested and stable features, you should be using this branch.
  * `main-docker` This branch is identical to the main branch with the exception of some docker components required to run a product in a local docker environment (excellent for testing a Formliss product without spending a lot of time setting up a local deployment environment).
  * `main-bare` This branch is designed for bare-metal (or, bare-metal-like) deployments. This branch is ideal for running on a single workstation, bare-metal dedicated server or VM.
  * `main-aws` This branch is optimized for deployment to AWS EC2 and similar environments
  * `main-azure` This branch is optimized for deployment to Azure and similar environments
  * `main-gcp` This branch is optimized for deployment to GCP (Google Cloud) and similar environments
  * `main-k8s`  This branch is ready for deployment in a K8s (Kubernetes) cluster
  * `test` - The test branch of the project. This is where new features are being staged and tested before moving to the stable `main` branch. If you're interested in using the latest features, that may (or may not) break your implementation, you should be using this branch.
  * `development` This is where new features are staged to ensure they are fully compatible with the rest of Formliss' products. Features found in development are likely to be integrated into the next stable release, but will not be moved into `test` or `main` until they are fully vetted and tested.
  * `skel` This branch is a skeleton branch that is used to create new branches for new projects. It is not intended to be used by anyone.
  * `doc` This is our documentation branch. Useful for anyone working on the documentation, but little else. New features may be announced here, but aren't necessarily going to be implemented in any other branch.
  * All other branches should _not_ be used by anyone, ever unless you are actively working on a specific feature for a Formliss product. These branches may contain broken, malfuctioning or unstable code. User beware: you can clone and run the code you find in any branch, but you should not expect it to work for any given purpose.