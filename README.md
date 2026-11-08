<!-- Header -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1b2733,100:8fa0b0&height=190&section=header&text=Lucas%20Burdier&fontSize=50&fontColor=ffffff&fontAlignY=36&animation=fadeIn&desc=Developer%20%C2%B7%203D%20Artist%20%C2%B7%20Lyon%2C%20France&descSize=17&descAlignY=58" width="100%" alt="Lucas Burdier">

<a href="https://github.com/lburdier"><img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&duration=2800&pause=900&color=8FA0B0&center=true&vCenter=true&width=620&lines=Computer+Science+student+at+YNOV+Lyon;Blender+Multiplayer%3A+edit+one+scene+together%2C+live;witness360%3A+camera+tracking+with+a+360+witness+cam;Building+EasyUV%2C+an+open-source+UV+unwrapper+in+Rust;easyuv-lint%3A+lint+your+3D+assets+in+CI;Desktop+tools%2C+web+systems+and+3D+assets;Looking+for+contributors%3A+come+build+with+me" alt="Typing intro"></a>

[![Website](https://img.shields.io/badge/lburdier.fr-portfolio-8fa0b0?style=flat-square&logo=googlechrome&logoColor=white)](https://lburdier.fr)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-lucas--burdier-8fa0b0?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucasburdier/)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-support-7a9080?style=flat-square&logo=ko-fi&logoColor=white)](https://ko-fi.com/D1D8X24NF)
[![Instagram](https://img.shields.io/badge/Instagram-luki__prox-888888?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/luki_prox/)
![Profile views](https://komarev.com/ghpvc/?username=lburdier&style=flat-square&color=7a9080&label=profile+views)

</div>

---

## About

Precision over decoration. I work at the intersection of technical rigor and cinematic sensibility: building desktop tools and web systems, crafting 3D assets, and designing experiences with deliberate restraint.

- Studying Computer Science at **YNOV Lyon**
- New: **[Blender Multiplayer](https://github.com/lburdier/blender-multiplayer)**, a Blender add-on to edit the same scene together in real time, on a LAN or over the internet with a private invite link
- New: **[witness360](https://github.com/lburdier/witness360-releases)**, a Windows and Mac app that tracks a shot with the help of a 360 camera mounted on the rig, then sends the camera and a matched HDRI to Blender
- Building **[EasyUV](https://github.com/lburdier/EasyUV)**, an open-source automatic UV unwrapper in Rust, with a Blender add-on
- Shipping **[easyuv-lint](https://github.com/lburdier/easyuv-lint)**: a CLI and GitHub Action that catches broken 3D assets (UV overlaps, texel density, polycount, scale) on every pull request
- Developing **[The Worst Roommate](https://github.com/lburdier/TheWorstRoommate)**, a PS1-style psychological horror game
- Shipping Windows apps with automatic updates: CV GEN, Umbra Editor, Claude Bridge

> **Let's build something together.** EasyUV welcomes contributors of every level: Rust, Python (Blender add-on), geometry, UI, docs and translations. Pick an issue, open a PR, or just say hi on [LinkedIn](https://www.linkedin.com/in/lucasburdier/).

---

## Latest projects

### Blender Multiplayer

**Several people, one Blender scene, live.** The host shares a private link, guests click it and land in the same scene, on the same network or across the internet (built-in relay, no port forwarding). Every change syncs as it happens: objects, meshes, materials, textures (even while painting), lights, animation. Each player sees who selects what, undo is shared, and the history, chat, autosaves and backups keep the project safe. Render settings stay personal to each PC. Blender 4.2+ and 5.x, pure Python, automatic updates through a Blender extension repository.

[![Download](https://img.shields.io/github/v/release/lburdier/blender-multiplayer?style=flat-square&label=download&color=8fa0b0)](https://github.com/lburdier/blender-multiplayer/releases/latest)
[![Website](https://img.shields.io/badge/install-extension%20repository-7a9080?style=flat-square&logo=blender&logoColor=white)](https://lburdier.github.io/blender-multiplayer/)

<table>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/lburdier/blender-multiplayer"><img src="https://raw.githubusercontent.com/lburdier/blender-multiplayer/main/docs/images/vue_hote.png" alt="Blender Multiplayer, host view"></a><br><sub><b>Host</b>: invite link, internet and LAN addresses, players, history, chat</sub></td>
    <td width="50%" align="center"><a href="https://github.com/lburdier/blender-multiplayer"><img src="https://raw.githubusercontent.com/lburdier/blender-multiplayer/main/docs/images/vue_invite.png" alt="Blender Multiplayer, guest view"></a><br><sub><b>Guest</b>: joined over the internet, the host's selection shown in red</sub></td>
  </tr>
</table>

### witness360

**Camera tracking helped by a 360 "witness" camera.** A 360 camera screwed onto the camera rig sees everything around the shot and records its gyroscope. witness360 syncs it to the shot by sound, tracks the plate, solves the camera with the 360 rotation, measures the real field of view on the 360 image, builds an HDRI matched to the plate's colour and exposure, then exports everything to Blender (Alembic .abc and a ready .blend). Insta360 .insv, any camera, S-Log3 / V-Log / LogC and more. Windows and macOS.

[![Download](https://img.shields.io/github/v/release/lburdier/witness360-releases?style=flat-square&label=download&color=8fa0b0)](https://github.com/lburdier/witness360-releases/releases/latest)

<p align="center">
  <a href="https://github.com/lburdier/witness360-releases"><img src="https://raw.githubusercontent.com/lburdier/witness360-releases/main/captures/06_solveur_quad.png" width="100%" alt="witness360 solver"></a>
  <br><sub><b>Solver</b>: 1803 3D points, 296 frames solved with the 360 gyroscope, error per tracker on the plate</sub>
</p>

<table>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/lburdier/witness360-releases"><img src="https://raw.githubusercontent.com/lburdier/witness360-releases/main/captures/02_medias_synchro.png" alt="witness360 sync"></a><br><sub><b>Sync</b>: the shot found in a 10 min 360 clip by sound, to the half millisecond</sub></td>
    <td width="50%" align="center"><a href="https://github.com/lburdier/witness360-releases"><img src="https://raw.githubusercontent.com/lburdier/witness360-releases/main/captures/11_hdri.png" alt="witness360 HDRI"></a><br><sub><b>HDRI</b>: 4096 x 2048 EXR from the 360, colour matched to the plate</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/lburdier/witness360-releases"><img src="https://raw.githubusercontent.com/lburdier/witness360-releases/main/captures/03_trackers_quad.png" alt="witness360 trackers"></a><br><sub><b>Trackers</b>: hundreds of points, forward-backward check</sub></td>
    <td width="50%" align="center"><a href="https://github.com/lburdier/witness360-releases"><img src="https://raw.githubusercontent.com/lburdier/witness360-releases/main/captures/12_export_blender.png" alt="witness360 export"></a><br><sub><b>Export</b>: animated camera, point cloud, plate and HDRI straight into Blender</sub></td>
  </tr>
</table>

---

## Featured projects

<div align="center">

<a href="https://github.com/lburdier/blender-multiplayer"><img src="assets/cards/pin-blender-multiplayer.svg" width="400" alt="Blender Multiplayer"></a>
<a href="https://github.com/lburdier/witness360-releases"><img src="assets/cards/pin-witness360-releases.svg" width="400" alt="witness360"></a>
<a href="https://github.com/lburdier/EasyUV"><img src="assets/cards/pin-easyuv.svg" width="400" alt="EasyUV"></a>
<a href="https://github.com/lburdier/easyuv-lint"><img src="assets/cards/pin-easyuv-lint.svg" width="400" alt="easyuv-lint"></a>
<a href="https://github.com/lburdier/cv-gen"><img src="assets/cards/pin-cv-gen.svg" width="400" alt="CV GEN"></a>
<a href="https://github.com/lburdier/instagrowth"><img src="assets/cards/pin-instagrowth.svg" width="400" alt="InstaGrowth"></a>
<a href="https://github.com/lburdier/TheWorstRoommate"><img src="assets/cards/pin-theworstroommate.svg" width="400" alt="The Worst Roommate"></a>

</div>

**Also shipping**

- **[Umbra Editor](https://github.com/lburdier/Umbra_Engine-releases)**: retro horror game editor for Windows (Direct3D 11).
- **[Claude Bridge](https://github.com/lburdier/claude-bridge-releases)**: multi-account Claude manager for Windows, with a Code workspace, node-based workflows and token stats.

---

## In pictures

<p align="center">
  <a href="https://github.com/lburdier/EasyUV"><img src="assets/easyuv.png" width="100%" alt="EasyUV unwrapping Suzanne"></a>
  <br><sub><b>EasyUV</b>: Suzanne unwrapped in one key press, 17 islands, UV score 88, checker preview on the model</sub>
</p>

<table>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/lburdier/cv-gen"><img src="https://raw.githubusercontent.com/lburdier/cv-gen/main/docs/screenshots/01-accueil.jpg" alt="CV GEN home"></a><br><sub><b>CV GEN</b>: home screen</sub></td>
    <td width="50%" align="center"><a href="https://github.com/lburdier/cv-gen"><img src="https://raw.githubusercontent.com/lburdier/cv-gen/main/docs/screenshots/04-editeur.jpg" alt="CV GEN editor"></a><br><sub><b>CV GEN</b>: live editor with ATS score</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/lburdier/cv-gen"><img src="https://raw.githubusercontent.com/lburdier/cv-gen/main/docs/screenshots/03-studio.jpg" alt="CV GEN design studio"></a><br><sub><b>CV GEN</b>: design studio, 500 templates</sub></td>
    <td width="50%" align="center"><a href="https://github.com/lburdier/instagrowth"><img src="https://raw.githubusercontent.com/lburdier/instagrowth/main/docs/screenshots/dashboard.png" alt="InstaGrowth stats"></a><br><sub><b>InstaGrowth</b>: stats and recent posts (demo data)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/lburdier/instagrowth"><img src="https://raw.githubusercontent.com/lburdier/instagrowth/main/docs/screenshots/instagram-profile.png" alt="InstaGrowth inside Instagram"></a><br><sub><b>InstaGrowth</b>: native buttons inside Instagram</sub></td>
    <td width="50%" align="center"><a href="https://github.com/lburdier/instagrowth"><img src="https://raw.githubusercontent.com/lburdier/instagrowth/main/docs/screenshots/leads.png" alt="InstaGrowth leads"></a><br><sub><b>InstaGrowth</b>: lead search and mini-CRM</sub></td>
  </tr>
</table>

---

## Stack

<div align="center">

**Code**

<img src="https://skillicons.dev/icons?i=rust,ts,js,react,electron,nodejs,python,kotlin&theme=dark" alt="Rust, TypeScript, JavaScript, React, Electron, Node.js, Python, Kotlin">
<br>
<img src="https://skillicons.dev/icons?i=html,css,php,java,postgres,git,githubactions,vscode&theme=dark" alt="HTML, CSS, PHP, Java, PostgreSQL, Git, GitHub Actions, VS Code">

**3D & design**

<img src="https://skillicons.dev/icons?i=blender,unreal,maya,ae,ps,figma&theme=dark" alt="Blender, Unreal Engine, Maya, After Effects, Photoshop, Figma">

</div>

<details>
<summary><b>Disciplines</b></summary>

<br>

**development**
- Desktop: Rust (egui), Electron, Windows tooling
- Web: HTML, CSS, JavaScript, TypeScript, React, PHP, Java, SQL, PL/pgSQL
- Mobile: Kotlin (Android)
- Scripting: Python
- Backend: Node.js
- Version control: Git / GitHub, GitHub Actions

**3d & visual**
- Modeling: Blender, Maya
- Texturing: Substance Painter / PBR pipeline
- Pipeline: Blender → Substance → DaVinci / ACES · EXR 32-bit output
- VFX & Compositing: After Effects

**design**
- Graphic Design: Photoshop, Figma
- Art Direction: DA systems, identity, motion principles
- Sound Design: cinematic, industrial, minimal

</details>

---

## GitHub

<div align="center">

<img src="assets/cards/stats.svg" height="165" alt="GitHub stats">
<img src="assets/cards/languages.svg" height="165" alt="Top languages">

<img src="https://streak-stats.demolab.com?user=lburdier&theme=transparent&hide_border=true&ring=8fa0b0&fire=7a9080&currStreakLabel=8fa0b0&sideLabels=aaaaaa&currStreakNum=dddddd&sideNums=dddddd&dates=888888" alt="Contribution streak">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lburdier/lburdier/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lburdier/lburdier/output/github-snake.svg">
  <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/lburdier/lburdier/output/github-snake-dark.svg">
</picture>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8fa0b0,100:1b2733&height=110&section=footer&animation=fadeIn" width="100%" alt="">
