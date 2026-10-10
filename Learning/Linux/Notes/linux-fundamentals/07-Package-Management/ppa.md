# PPA

## Overview
PPA means Personal Package Archive, a repository commonly hosted on Launchpad for Ubuntu packages.
Adding a PPA extends the host's software trust boundary beyond its default repositories.

## Common Usage
Review the publisher and supported distribution release before adding a PPA.
```bash
apt policy nginx
grep -R '^deb ' /etc/apt/sources.list.d/
```
Do not add an unverified PPA to production just to obtain a newer package.

## SRE Relevance
Third-party archives can introduce unreviewed code, upgrade conflicts, and availability dependencies.
Prefer approved vendor repositories or internally mirrored packages with ownership and rollback plans.

## Quick Examples
Ubuntu's `add-apt-repository` can add a PPA; remove it when it is no longer approved or required.

## Common Flags
Not applicable; a PPA is a repository type, not a command option.

## Related Topics
- [Add APT repository](add-apt-repository.md)
- [Remove option](remove-option.md)
- [APT](apt.md)
