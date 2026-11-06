# Owner editing contracts

Back up an existing blog's full theme and Layout settings before installing a theme. Development builds belong on a test blog. Theme XML and demo post-content XML are different files and use different import screens.

## Identity and homepage

Edit the blog title and description in Blogger Settings. The Header widget controls an optional logo; text remains available to assistive technology. PageList provides native page navigation. In Layout, open **Homepage introduction** to change the welcome copy and topic links. Link topics to `/search/label/<encoded-label>` using the labels your own posts actually have. Theme Designer exposes accent/background/text colors; recheck contrast when changing them.

The introduction is editable in Layout; structural rails, notebook frames, topic navigation and other home composition details also live in `themes/<slug>/home.html` for source-level changes. Native topic links must match the labels used on your real posts.

The first post on the home page supplies the featured story. It is not duplicated in the first page's latest grid. Changing the Blogger posts-per-page setting changes the native pagination size without any separate JavaScript setting.

## Article formats

Each theme's `post-template.html` is an editable starting point. Paste it into a post's HTML view or save it in Blogger's post-template setting. Supply your own facts, credits, source links and disclosures. Keep the documented class/data attributes for enhancements you want to use; deleting the complete feature block is also supported.

- Saffron: `.recipe-name`, `.recipe-ingredients label`, `.recipe-instructions li` and an article image supply optional Recipe metadata. ISO duration attributes such as `data-prep-time="PT15M"` are optional. Missing required content omits that metadata. Tested recipes and suitable dish imagery are the author's responsibility.
- Lesson: objectives, exercises and learning-path links are ordinary HTML. Course indexes and sequence links are owner-maintained; this is not an LMS or access-control service.
- Bench: review facts, specifications, methodology and affiliate disclosures are entered by the author. No score, offer or aggregate rating is generated automatically.
- Ledger: the local calculator subtracts expenses from income. It has no storage, submission or remote request. State the currency and assumptions around any real financial example.
- Soundboard: optional media buttons use `data-video-src` and `data-video-title`; only documented HTTPS YouTube privacy-enhanced or Vimeo embed URLs are accepted. The default demonstration does not load third-party media.
- Other themes: project checklists, book/plant profiles, event details, credit tables and spoiler disclosures use semantic HTML. Replace irrelevant sections completely rather than retaining fake example data.

The table of contents appears only when at least three non-empty article headings exist. Existing heading IDs are preserved; generated IDs avoid collisions. Print buttons use the browser's print function and hide navigation/comment clutter through the print stylesheet, applied after the theme styles to keep light and dark designs readable on paper.

## Images and external services

The included cover set is original illustration, not photography or evidence of actual product testing. Upload or link your own properly licensed media for a real publication. Give images meaningful alt text. Payments, bookings, donation checkout, podcast hosting, restricted course access and email subscriptions use the owner's chosen external services; the theme does not create accounts or backends for them.

Check native comments, search, labels, mobile layout and a later pagination page after installation. To roll back, restore the saved theme and recorded widget settings; published posts need not change.
