automation - cypress
===================
Working example of e2e testing with [cypress](https://docs.cypress.io)

## Commands
* **installation:** `yarn install`
* **e2e:** `yarn e2e` *starts cypress e2e suite*

## Setup brower
* In `package.json` you will have to define browser target so cypress can execute it.

```typescript
  "e2e:run": "cross-env CYPRESS_RETRIES=3 cypress run --browser /usr/local/bin/chrome", // chrome browser
  "e2e": "http://localhost:8080 e2e:run"
```

## Scaffolding
* * integration (folder) `functional tests`
* * screenshots (folder) `screenshots`
* * support (folder) `additional stuff for cypress`
* * * commands.js (file) `additional commands registered like login to be available in cypress context`
