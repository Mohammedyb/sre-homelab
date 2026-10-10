# Linux Overview

## What Is Linux?

Linux is an open-source, Unix-like operating system. Strictly speaking, **Linux** is the kernel: the core software that manages hardware and provides services to programs. A complete operating system combines the Linux kernel with system tools, libraries, and applications. These combinations are commonly called **Linux distributions** or **distros**.

Linux is used on servers, desktops, cloud platforms, embedded devices, and supercomputers. It is valued for its flexibility, stability, security features, and broad range of distributions.

## Main Components

- **Kernel** — Manages processes, memory, devices, filesystems, and communication between software and hardware.
- **Shell** — Accepts commands and starts programs. Common shells include Bash, Zsh, and Fish.
- **Utilities and libraries** — Provide common tools and reusable functionality for the system and applications.
- **Filesystem** — Organizes files and directories in a single hierarchy that starts at `/`.
- **Applications and services** — Programs used by people or run in the background to provide system functions.
- **Desktop environment (optional)** — Provides a graphical interface, including windows, panels, and menus. Examples include GNOME and KDE Plasma.

## Distributions

A Linux distribution packages the kernel with system software, a package manager, and often a desktop environment and default applications.

Examples include:

- **Ubuntu** and **Linux Mint** — Popular general-purpose distributions.
- **Debian** — A community distribution known for its stability.
- **Fedora** — A community distribution featuring relatively recent technologies.
- **Red Hat Enterprise Linux (RHEL)** — A commercially supported distribution for enterprise use.
- **Arch Linux** — A flexible distribution that expects users to configure much of the system themselves.

Distributions differ in their goals, release schedules, supported software, and administration tools, but many share the same Linux fundamentals.

## Basic Concepts

### The Command Line

Commands are entered into a terminal through a shell. For example:

```bash
pwd
```

`pwd` prints the current working directory. Commands can accept options and arguments:

```bash
ls -l /home
```

Here, `ls` lists directory contents, `-l` requests a detailed format, and `/home` is the directory to list.

### Users and Permissions

Linux is a multi-user operating system. Files and processes have owners and permissions that control who can read, modify, or execute them. The **root** account is the system administrator and has broad privileges. Use administrator privileges carefully, commonly through `sudo`.

### Processes and Services

A running program is a **process**. A background process that provides an ongoing system function is often called a **service** or **daemon**. Linux provides tools to inspect and manage processes and services.

### Packages

Software is commonly installed and updated through a distribution's **package manager**. For example, Debian-based systems use APT, while Fedora uses DNF. Package managers help resolve dependencies and keep software organized.

## Getting Started Commands

| Command | Purpose |
| --- | --- |
| `pwd` | Print the current directory |
| `ls` | List files and directories |
| `cd` | Change the current directory |
| `mkdir` | Create a directory |
| `touch` | Create an empty file or update a file's timestamp |
| `cp` | Copy files or directories |
| `mv` | Move or rename files or directories |
| `rm` | Remove files or directories |
| `man` | Read a command's manual page |

> **Caution:** Commands such as `rm` can permanently delete data. Check the target path before running commands that modify or remove files.

## Key Takeaways

- Linux is the kernel; a distribution combines it with tools and applications to form a complete operating system.
- The terminal and shell provide a powerful way to work with Linux.
- Users, permissions, processes, services, and packages are core administration concepts.
- The command line is consistent across many distributions, even when their package managers and configuration tools differ.
