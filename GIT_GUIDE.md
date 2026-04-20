# Git & GitHub Setup for Advanced Python Project

## 🎯 Goal

To upload a local Python project to GitHub with proper structure and best practices.

---

## 🧠 Key Concepts

### Git vs GitHub

* **Git** → Local version control system (tracks changes)
* **GitHub** → Cloud platform to store and share code

---

## 🚀 Steps to Push Project to GitHub

### 1. Initialize Git

```bash
git init
```

**Why:** Converts your folder into a Git repository.

---

### 2. Create `.gitignore`

Add:

```
.venv/
env/
__pycache__/
*.pyc
```

**Why:** Prevents unnecessary files from being tracked.

---

### 3. Add Files

```bash
git add .
```

**Why:** Moves files to staging area.

---

### 4. Commit Changes

```bash
git commit -m "Initial commit"
```

**Why:** Saves a snapshot of your project.

---

### 5. Connect to GitHub

```bash
git remote add origin https://github.com/your-username/repo-name.git
```

**Why:** Links local repo to GitHub.

---

### 6. Push to GitHub

```bash
git branch -M main
git push -u origin main
```

**Why:** Uploads your code to GitHub.

---

## ⚠️ Common Issue & Fix

### Error:

```
rejected (fetch first)
```

### Fix:

```bash
git pull origin main --rebase
git push -u origin main
```

**Why:** Syncs local and remote repositories.

---

## ❌ Why `.venv` Should Not Be Pushed

* Very large size (100MB+)
* System-specific (won’t work for others)
* Makes repo messy

### ✅ Instead:

Use:

```bash
pip freeze > requirements.txt
```

---

## 📌 Best Practices

* Create `.gitignore` before `git add .`
* Keep repo clean and structured
* Add meaningful commit messages
* Include a `README.md`
* Add real-world examples (not just notes)

---

