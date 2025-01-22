## Installation

Open a terminal and run:

```sh
npm install pnpm
cd frontend
pnpm install
pnpm build
cd ..
pip install -e ./backend
chainlit run demo.py -w
```

If this opens the app in your browser at http://localhost:8000, you're all set!

## Development 

Anytime you make changes, you will have to rebuild the frontend and redo a pip install so the backend can pick up the changes as well.

```
cd frontend
pnpm build
cd ..
pip install -e ./backend
sh scripts/kill_demo.sh
chainlit run demo.py -w
```
