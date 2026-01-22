# AGENTS.md - Mini Arcade Development Guidelines

This repository contains a collection of HTML5 browser games. All games are self-contained single HTML files with inline CSS and JavaScript. No build tools, no package managers, no external dependencies required for core functionality.

## Build, Lint, and Test Commands

This project uses no build tools or package managers. Each game is a standalone HTML file.

### Running a Game
- **Direct browser**: Open the `.html` file directly in any modern browser (Chrome, Firefox, Safari, Edge)
- **Via local server**: `npx serve .` or `python -m http.server 8000` in the project root
- **Specific game**: Open `index.html` to browse all games, or open individual game files directly

### Testing
No automated tests exist. Manual testing must verify:
- Game loads without console errors (check F12 developer console)
- All game controls work (mouse, keyboard, touch input)
- Responsive design works on different screen sizes (desktop, tablet, mobile)
- No external CDN dependencies break (fonts, libraries)
- Game flow: start -> play -> pause/resume -> win/lose -> restart

### Code Validation
- **HTML**: Use W3C Validator (https://validator.w3.org) for HTML structure
- **JavaScript**: Enable strict mode, check console for linting errors
- **CSS**: Verify in browser dev tools for layout issues

## Code Style Guidelines

### HTML Structure
- Use lowercase for HTML tags and attributes
- Always include `lang` attribute on `<html>` (e.g., `lang="zh-TW"`)
- Include meta charset (`<meta charset="UTF-8">`) and viewport tags for mobile support
- Close all tags properly, use self-closing syntax for void elements
- Structure: `<!DOCTYPE html>` -> `<html>` -> `<head>` with `<style>` -> `<body>` -> `<script>`

### CSS
- Define CSS variables in `:root` for colors and shared values
- Use CSS custom properties for theming (see `index.html` for color pattern)
- Prefer flexbox and CSS grid for layouts over floats
- Include vendor prefixes only when necessary (`-webkit-` for iOS Safari)
- Use `box-sizing: border-box` globally (`* { box-sizing: border-box; }`)
- Mobile-first approach with `@media` queries for larger screens
- Handle `touch-action: none` for game canvases to prevent scrolling
- Use `clamp()` for responsive font sizes when appropriate
- Avoid inline styles; keep all CSS in `<style>` block in `<head>`

### JavaScript
- Use `const` and `let` instead of `var`; avoid `var` entirely
- Use arrow functions for callbacks and anonymous functions
- Prefix private/internal variables with underscore (e.g., `_gameState`)
- Event handlers: use named functions for proper cleanup (removeEventListener)
- Game loop: use `requestAnimationFrame` with delta time calculation for consistent speed
- Canvas rendering: batch draw calls and use `save()`/`restore()` for state changes
- Touch/mouse input: handle both with pointer events or separate handlers
- Always declare strict mode: `'use strict';` at the top of script blocks

### Naming Conventions
- **CSS classes**: kebab-case (`.game-card`, `.start-btn`, `.score-display`)
- **JavaScript variables/functions**: camelCase (`startGame`, `updateScore`, `gameLoop`)
- **Constants**: SCREAMING_SNAKE_CASE for config values (`GRID_SIZE`, `MAX_SCORE`)
- **IDs**: camelCase (`#gameCanvas`, `#startScreen`, `#scoreDisplay`)
- **File names**: lowercase with underscores or hyphens (`snack.html`, `air_hockey.html`)

### Error Handling
- Wrap canvas operations in try-catch for context errors
- Provide fallback for missing features (e.g., no Web Audio API, no touch support)
- Log errors with descriptive messages: `console.error('Failed to init:', err)`
- Never swallow errors silently; always handle or log them
- Handle `resize` events to prevent canvas stretching and blurriness
- Validate user input before processing (keyboard, touch coordinates)

### Performance
- Cache DOM queries outside render loops (e.g., `const canvas = document.getElementById(...)`)
- Use `requestAnimationFrame` for all game animations, never `setInterval`
- Clean up event listeners and cancel `requestAnimationFrame` on game end
- Avoid memory leaks: nullify references when destroying game objects
- Use `offscreenCanvas` for complex pre-rendering if needed
- Minimize canvas state changes; batch similar operations together

### Internationalization
- UI text in Traditional Chinese with English fallbacks where appropriate
- Use `lang="zh-TW"` on `<html>` element
- Date/number formatting should consider Chinese locale
- Consistent terminology: use established Chinese game terms (e.g., "分數" for score)

## File Organization

- **Each game** in its own `.html` file named descriptively
- **Inline CSS** in `<style>` tags within `<head>`
- **Inline JS** in `<script>` tags before `</body>`
- **No external JS/CSS files** per game (keep self-contained)
- **Shared patterns** can be duplicated; no common modules required
- **3D games** go in `3D-test/` directory with local library copies

## Game-Specific Patterns

### Standard Game Structure
1. Start screen with title, instructions, and start button
2. Canvas-based rendering for action games
3. State machine: `menu` -> `playing` -> `paused`/`gameover`
4. Score display during gameplay
5. Win/lose screen with restart option
6. Touch controls for mobile, keyboard controls for desktop

### Common Game Elements
- Navigation bar with back link to `index.html`
- Score display in prominent location
- Control instructions panel
- Start/Pause/Restart buttons
- Mobile D-pad or swipe controls
- Responsive canvas sizing

### Physics & Game Logic
- Use delta time for frame-rate independent movement
- Implement collision detection appropriate to game type
- Balance difficulty progression (speed increase, difficulty levels)
- Save high scores to `localStorage` when appropriate

## Development Workflow

1. Create new game file following existing patterns (copy structure from similar game)
2. Test in Chrome, Firefox, Safari, and mobile browsers
3. Update `index.html` with new game card in appropriate category
4. Test complete game flow: start -> play -> win/lose -> restart
5. Verify no console errors in browser dev tools
6. Test responsiveness on multiple screen sizes

## Adding New Games

When adding a new game:
1. Create `.html` file in root directory (or `3D-test/` for 3D games)
2. Follow the standard HTML template structure
3. Add navigation back to index: `<a class="back-link" href="index.html">← 回到遊戲入口</a>`
4. Use consistent game panel layout from existing games
5. Add game card to `index.html` in correct category (SOLO, VERSUS, or MIND)
6. Choose appropriate color class: `color-single`, `color-multi`, `color-board`, `color-action`
7. Test thoroughly before committing

## Browser Compatibility

- Target: Modern browsers (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- Fallback: Graceful degradation for older browsers
- Mobile: iOS Safari and Chrome for Android
- Touch: Support both touch events and mouse events
- Audio: Web Audio API with fallback to silent operation
