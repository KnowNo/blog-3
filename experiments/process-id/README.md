1. batch vs shell on launching another script
   * call -> source: run in same process, and continue
   * default -> exec: run in same process, and exit immediately
   * start -> default: run in a new process, and continue

2. If a parent process already exit, the child process run in background's parent process become user's init process
