# Git & GitHub Setup Guide (General Purpose)

## 🎯 Goal

To upload any local project to GitHub using proper version control practices.

---

## 🧠 Key Concepts

### Git vs GitHub

* **Git** → Tracks changes locally (version control system)
* **GitHub** → Cloud platform to store, manage, and share repositories

---

## 🚀 Standard Workflow

### 1. Initialize Git

```bash
git init
```

**Why:** Starts version tracking in your project folder.

---

### 2. Create `.gitignore`

Example:

```
.venv/
env/
__pycache__/
*.pyc
node_modules/
dist/
```

**Why:** Prevents unnecessary/system files from being tracked.

---

### 3. Add Files

```bash
git add .
```

**Why:** Moves selected files to staging.

---

### 4. Commit Changes

```bash
git commit -m "Initial commit"
```

**Why:** Saves a snapshot of your project.

---

### 5. Connect to Remote Repository

```bash
git remote add origin https://github.com/your-username/repo-name.git
```

**Why:** Links your local repo to GitHub.

---

### 6. Push Code

```bash
git branch -M main
git push -u origin main
```

**Why:** Uploads your project to GitHub.

---

## ⚠️ Common Error & Fix

### Error:

```
rejected (fetch first)
```

### Fix:

```bash
git pull origin main --rebase
git push -u origin main
```

**Why:** Syncs local and remote repositories before pushing.

---

## 🔄 Daily Workflow (After Initial Setup)

```bash
git add .
git commit -m "your message"
git push
```

---

## ❌ What NOT to Push

Avoid committing:

* Virtual environments (`.venv/`, `env/`)
* Cache files (`__pycache__/`)
* Large dependencies (`node_modules/`)
* System files

---

## ✅ Best Practice for Dependencies

Instead of uploading dependencies:

* Python:

  ```bash
  pip freeze > requirements.txt
  ```

* Node.js:

  ```
  package.json
  ```

---

## 📁 Recommended Project Structure

```
project-name/
│
├── src/ or main code folders
├── tests/
├── requirements.txt / package.json
├── README.md
├── .gitignore
```

---

## 📌 Best Practices

* Create `.gitignore` before `git add .`
* Use clear and meaningful commit messages
* Keep repository clean and organized
* Add `README.md` explaining your project
* Commit regularly

---

## 🧠 Final Insight

Git is not just for saving code —
it’s for:

* Tracking changes
* Collaborating
* Showcasing your work professionally

---
