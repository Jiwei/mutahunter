<div align="center">
  <h1>Mutahunter</h1>

  Open-Source Language Agnostic LLM-based Mutation Testing for Automated Software Testing
  
  Maintained by [CodeIntegrity](https://www.codeintegrity.ai). Anyone is welcome to contribute. 🌟

  [![GitHub license](https://img.shields.io/badge/License-AGPL_3.0-blue.svg)](https://github.com/yourcompany/mutahunter/blob/main/LICENSE)
  [![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.gg/S5u3RDMq)
  [![Twitter](https://img.shields.io/twitter/follow/CodeIntegrity)](https://twitter.com/CodeIntegrity)
  [![Unit Tests](https://github.com/codeintegrity-ai/mutahunter/actions/workflows/test.yaml/badge.svg)](https://github.com/codeintegrity-ai/mutahunter/actions/workflows/test.yaml)
  <a href="https://github.com/codeintegrity-ai/mutahunter/commits/main">
  <img alt="GitHub" src="https://img.shields.io/github/last-commit/codeintegrity-ai/mutahunter/main?style=for-the-badge" height="20">
  </a>
</div>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Roadmap](#roadmap)
- [Cash Bounty Program](#cash-bounty-program)

## Overview

Mutation testing is used by big tech companies like [Google](https://research.google/pubs/state-of-mutation-testing-at-google/) to ensure the robustness of their test suites. With Mutahunter, we aim to empower other companies and developers to use this powerful tool to enhance their test suites and improve software quality.

Mutation testing verifies the effectiveness of your test cases by creating small changes, or “mutants,” in the code and checking if the test cases can catch these changes. Unlike line coverage, which only shows code execution, mutation testing reveals how well the code is tested.

Mutahunter uses LLM models to inject context-aware faults into your codebase. This AI-driven approach produces fewer equivalent mutants, mutants with higher fault detection potential, and those with higher coupling and semantic similarity to real faults, ensuring comprehensive and effective testing.

## Features

- **Extreme Mutation Testing:** Leverages language agnostic [TreeSitter](https://tree-sitter.github.io/) parser to apply extreme mutations to the codebase without using LLMs. [Research](https://arxiv.org/abs/2103.08480) shows that this approach is effective at detecting pseudo-tested methods with significantly lower computational cost. Currently supports Python, Java, JavaScript, and Go. Check the [scheme files](/src/mutahunter/core/pilot/aider/queries/) to see the supported operators. We welcome contributions to add more operators and languages.
- **LLM Context-aware Mutations:** Utilizes LLM models to generate context-aware mutants. [Research](https://arxiv.org/abs/2406.09843) indicates that LLM-generated mutants have higher fault detection potential, fewer equivalent mutants, and higher coupling and semantic similarity to real faults. It uses a map of your entire git repository to generate contextually relevant mutants using [aider's repomap](https://aider.chat/docs/repomap.html). Supports self-hosted LLMs, Anthropic, OpenAI, and any LLM models via [LiteLLM](https://github.com/BerriAI/litellm).
- **Change-Based Testing:** Runs mutation tests on modified files and lines based on the latest commit or pull request changes, ensuring that only relevant parts of the code are tested.
- **Language Agnostic:** Compatible with languages that provide coverage reports in Cobertura XML, Jacoco XML, and lcov formats. Extensible to additional languages and testing frameworks.
- **Detailed Mutant Reports:** Provides comprehensive reports on mutation coverage, killed mutants, and survived mutants.

## Recommended Mutation Testing Process

![Workflow](/images/diagram.svg)

1. **Achieve High Line Coverage:** Ensure your test suite has high line coverage, preferably 100%.

2. **Strict Mutation Testing:** Use strict mutation testing to improve mutation coverage without additional cost. Utilize the `--only-mutate-file-paths` flag for targeted testing on critical files.

3. **LLM-Based Mutation Testing on Changed Files:** Inject context-aware mutants using LLMs on changed files during pull requests as the final line of defense. Use the `--modified-files-only` flag to focus on recent changes. In this way it will make the mutation testing significantly **faster** and **cost effective.**

## Getting Started

```bash
# Install Mutahunter package via GitHub. Python 3.11+ is required.
$ pip install git+https://github.com/codeintegrity-ai/mutahunter.git

# Work with GPT-4o on your repo
$ export OPENAI_API_KEY=your-key-goes-here

# Or, work with Anthropic's models
$ export ANTHROPIC_API_KEY=your-key-goes-here

# Run Mutahunter on a specific file. 
# Coverage report should correspond to the test command.
$ mutahunter run --test-command "pytest tests/unit" --code-coverage-report-path "coverage.xml" --only-mutate-file-paths "app_1.py" "app_2.py"

# Run mutation testing on modified files based on the latest commit
$ mutahunter run --test-command "pytest tests/unit" --code-coverage-report-path "coverage.xml" --modified-files-only

.  . . . .-. .-. . . . . . . .-. .-. .-. 
|\/| | |  |  |-| |-| | | |\|  |  |-  |(  
'  ` `-'  '  ` ' ' ` `-' ' `  '  `-' ' ' 

2024-07-05 00:26:13,420 INFO: 📊 Line Coverage: 100% 📊
2024-07-05 00:26:13,420 INFO: 🎯 Mutation Coverage: 61.54% 🎯
2024-07-05 00:26:13,420 INFO: 🦠 Total Mutants: 13 🦠
2024-07-05 00:26:13,420 INFO: 🛡️ Survived Mutants: 5 🛡️
2024-07-05 00:26:13,420 INFO: 🗡️ Killed Mutants: 8 🗡️
2024-07-05 00:26:13,421 INFO: 🕒 Timeout Mutants: 0 🕒
2024-07-05 00:26:13,421 INFO: 🔥 Compile Error Mutants: 0 🔥
2024-07-05 00:26:13,421 INFO: 💰 Total Cost: $0.00583 USD 💰
2024-07-05 00:26:13,421 INFO: Report saved to logs/_latest/mutation_coverage.json
2024-07-05 00:26:13,421 INFO: Report saved to logs/_latest/mutation_coverage_detail.json
2024-07-05 00:26:13,421 INFO: Mutation Testing Ended. Took 43s
```

### Examples

Go to the examples directory to see how to run Mutahunter on different programming languages:

Check [Java Example](/examples/java_maven/) to see some interesting LLM-based mutation testing examples.

- [Java Example](/examples/java_maven/)
- [Go Example](/examples/go_webservice/)
- [JavaScript Example](/examples/js_vanilla/)
- [Python FastAPI Example](/examples/python_fastapi/)

Feel free to add more examples! ✨

## Mutant Report

Check the logs directory to view the report:

- `mutants.json` - Contains the list of mutants generated.
- `mutation_coverage.json` - Contains the mutation coverage percentage.
- `mutation_coverage_detail.json` - Contains detailed information per source file.

## Cash Bounty Program

Help us improve Mutahunter and get rewarded! We have a cash bounty program to incentivize contributions to the project. Check out the [bounty board](https://docs.google.com/spreadsheets/d/1cT2_O55m5txrUgZV81g1gtqE_ZDu9LlzgbpNa_HIisc/edit?gid=0#gid=0) to see the available bounties and claim one today!

## Roadmap

- [x] **Fault Injection:** Utilize advanced LLM models to inject context-aware faults into the codebase, ensuring comprehensive mutation testing.
- [x] **Language Support:** Expand support to include various programming languages.
- [x] **Support for Other Coverage Report Formats:** Add compatibility for various coverage report formats.
- [x] **Change-Based Testing:** Implement mutation testing on modified files based on the latest commit or pull request changes.
- [x] **Extreme Mutation Testing:** Apply mutations to the codebase without using LLMs to detect pseudo-tested methods with significantly lower computational cost.
- [ ] **Mutant Analysis:** Automatically analyze survived mutants to identify potential weaknesses in the test suite. Any suggestions are welcome!
- [ ] **CI/CD Integration:** Develop connectors for popular CI/CD platforms like GitHub Actions.
- [ ] **Automatic PR Bot:** Create a bot that automatically identifies bugs from the survived mutants list and provides fix suggestions.

## Acknowledgements

Mutahunter makes use of the following open-source libraries:

- [aider](https://github.com/paul-gauthier/aider) by Paul Gauthier, licensed under the Apache-2.0 license.
- [TreeSitter](https://github.com/tree-sitter/tree-sitter) by TreeSitter, MIT License.
- [LiteLLM](https://github.com/BerriAI/litellm) by BerriAI, MIT License.

For more details, please refer to the LICENSE file in the repository.
