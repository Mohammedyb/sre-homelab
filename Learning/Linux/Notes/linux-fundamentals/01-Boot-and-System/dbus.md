# D-Bus

## Overview
D-Bus (Desktop Bus) is an inter-process communication (IPC) system that lets local processes exchange messages.
System services and desktop applications can expose named APIs over a D-Bus bus.

## Common Usage
List bus names when diagnosing a service that exposes its control interface through D-Bus.
```bash
busctl list
busctl status org.freedesktop.systemd1
```
Use a host's local system bus; do not expose it remotely without a deliberate security design.

## SRE Relevance
Service integrations can fail when a bus, name, or policy is unavailable.
Inspect bus reachability and service logs while avoiding broad permission changes.

## Quick Examples
`busctl introspect SERVICE OBJECT_PATH` lists methods and properties exposed at an object path.

## Common Flags
| Flag | Description |
| --- | --- |
| `busctl --system` | Connect explicitly to the system bus |

## Related Topics
- [systemd](systemd.md)
- [Init manager](init-manager.md)
