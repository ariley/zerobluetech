import rss from '@astrojs/rss'
import { SITE_TITLE, SITE_DESCRIPTION } from '../config.ts'
import { sortedPosts } from '@/js/util.js'

// https://docs.astro.build/en/guides/rss/#using-glob-imports
export function GET (context) {
  const postImportResult = import.meta.glob('../posts/**/*.{md,mdx}', { eager: true })
  const posts = sortedPosts(Object.values(postImportResult))
  // Filter out system pages that don't have proper content
  const blogPosts = posts.filter(post =>
    post.frontmatter.title &&
    post.frontmatter.description &&
    (post.frontmatter.pubDate || post.frontmatter.date) &&
    post.frontmatter.permalink
  )
  return rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    // site: import.meta.env.SITE,
    site: context.site,
    items: blogPosts.map((post) => ({
      link: post.frontmatter.permalink,
      title: post.frontmatter.title,
      pubDate: new Date(post.frontmatter.pubDate || post.frontmatter.date),
      description: postSummary(post)
    }))
  })
}

function postSummary (post) {
  // Get content - handle different content types
  let content = ''
  if (typeof post.compiledContent === 'function') {
    content = post.compiledContent()
  } else if (typeof post.rawContent === 'function') {
    content = post.rawContent()
  } else if (post.body) {
    content = post.body
  } else {
    content = post.frontmatter.description || ''
  }

  // Ensure content is a string
  if (typeof content !== 'string') {
    content = String(content)
  }

  return content
    // you can delete the below if you want to include
    // the entire blog post in your RSS feed. Note that
    // many RSS readers cache results, so readers who read
    // via RSS only won't see post edits.
    .slice(0, 1000)
    .split(' ')
    .slice(0, 100) // about 100 words
    .join(' ')
    // remove unclosed tags so that the 'Read more' link renders correctly
    .replace(/<\/[a-zA-Z]+$/, '')
    + ` &hellip; <a href="${post.frontmatter.permalink}">Read more</a>`
}
