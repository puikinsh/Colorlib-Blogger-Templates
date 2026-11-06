# Shared source, distinct publishing experiences

Each generated XML embeds the shared CSS/runtime and the theme's own styling and welcome content. A build performs literal, checked token substitution; unresolved tokens fail the build. XML is parsed before output. The result imports as one theme without fetching collection code at runtime.

Native Blogger `Header`, `PageList`, `HTML` and `Blog` widgets handle identity, navigation, owner-editable home content and publishing. The home hero promotes the first server-rendered post; the latest grid excludes that already-featured post on the first page. Later pages show the full native page. Older/Newer URLs are not rewritten, counted or guessed, so tied timestamps and shortened pages remain Blogger's responsibility.

Articles use one renderer for desktop and the legacy mobile entry point. Native Blogger comment includables are retained from the maintained Pixel source. Blogger's `all-head-content` owns canonical and Open Graph output. The theme supplies an escaped `WebSite` record and an escaped `BlogPosting` record for actual post pages; static pages do not masquerade as posts.

The runtime adds a TOC with collision-free generated IDs, checklist reset, print controls, conditional Recipe metadata, an explicitly local arithmetic example and opt-in media embeds. Most niche formats rely on semantic HTML, tables, checklists and native `details`. Calculators are not forms: their inputs cannot be submitted to Blogger when JavaScript is disabled. Media URLs are restricted to HTTPS embed URLs on the supported providers.

Every theme owns a different home composition, typography, layout overrides and post-format contract. Shared helpers do not dictate that a lesson, product review and recipe share the same information hierarchy. Original SVG covers avoid a dependency on stock-photo hosts and keep demonstration asset provenance explicit.

All twenty themes share a `home.html` composition between native XML and static review output through a single featured-post slot; see [design directions](DESIGN-DIRECTIONS.md).

The local HTML renderer supplies representative data for visual review. It deliberately does not interpret Blogger expressions or prove platform compatibility. The validation report separates deterministic source/browser checks from actual Blogger import, native commenting and public-demo checks.

`core/print.css` is appended after every theme override in both output types. Static category pages are generated from each configured topic and actual demo label; links preserve their topic instead of all opening the same sample category. `tools/review.py` generates desktop/mobile comparison boards from live preview pages.
