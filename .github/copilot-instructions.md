# Parakeet - Hello World Example Repository

This is a minimal "Hello World Example with few vulns" repository containing only basic documentation. Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Repository Overview
Parakeet is a minimal demonstration repository designed as a simple example project. The codebase consists of:
- A single README.md file with basic project description
- No build system, dependencies, or complex application code
- No automated tests or CI/CD pipelines

## Working Effectively
### Repository Structure
- **Root directory**: Contains only README.md
- **No build system**: There are no package.json, Makefile, or other build configuration files
- **No dependencies**: No external libraries or frameworks to install
- **No source code**: This is a documentation-only repository

### Basic Operations
- Clone and navigate: 
  - `git clone <repository-url>`
  - `cd parakeet`
- View repository contents:
  - `ls -la` - shows only README.md and .git directory
  - `cat README.md` - displays the basic project description
- Standard git operations work normally:
  - `git status`
  - `git log`
  - `git branch`

### What You CAN Do
- Read and modify the README.md file
- Add new documentation files
- Create new directories and files
- Use standard git commands for version control
- Add GitHub workflows in .github/workflows/ if needed

### What You CANNOT Do
- Build the project (no build system exists)
- Run tests (no test suite exists)
- Install dependencies (none exist)
- Start a server or application (no application code exists)
- Run linting tools (no code to lint)

## Validation
Since this is a minimal repository with no executable code:
- **File validation**: Ensure any new files are properly formatted and readable
- **Git validation**: Verify git operations complete successfully
- **Documentation validation**: Check that README.md and any new documentation is clear and accurate

## Common Tasks
The following are outputs from frequently run commands in this repository:

### Repository root listing
```bash
ls -la
total 16
drwxr-xr-x 3 runner docker 4096 Sep  5 20:53 .
drwxr-xr-x 3 runner docker 4096 Sep  5 20:53 ..
drwxr-xr-x 7 runner docker 4096 Sep  5 20:53 .git
-rw-r--r-- 1 runner docker   46 Sep  5 20:53 README.md
```

### README.md contents
```bash
cat README.md
# parakeet
Hello World Example with few vulns
```

### Git status (clean state)
```bash
git status
On branch copilot/fix-3
Your branch is up to date with 'origin/copilot/fix-3'.
nothing to commit, working tree clean
```

## Development Workflow
When making changes to this repository:
1. **Always start** by reading the README.md to understand the current state
2. **Check git status** before making any changes
3. **Create or modify files** as needed using standard text editors
4. **Validate changes** by reading files back and checking git diff
5. **Commit changes** with descriptive messages
6. **No build or test steps required** - this repository has no executable code

## Important Notes
- This repository is intentionally minimal and serves as an example or template
- Do not attempt to add complex build systems unless specifically required
- Focus on clear documentation and simple file operations
- Any "vulns" mentioned in the README likely refer to intentional security examples for educational purposes
- Always verify file contents after making changes since there are no automated validation tools