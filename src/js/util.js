'use strict'

// alternative: https://github.com/mdevils/html-entities
import { decodeHTML } from 'entities'

// if you need a fancier one, you could use https://github.com/sindresorhus/slugify
export function urlifyToken (s) {
  return s.toLowerCase().replaceAll(' ', '-')
}

// https://github.com/DylanPiercey/strip
const htmlReg = /<\/?([a-z][a-z0-9]*)\b[^>]*>?/gi
const commentReg = /<!--.+-->/gi
export function stripHTML (html = '') {
  // Ensure html is a string
  if (typeof html !== 'string') {
    html = String(html || '')
  }
  return decodeHTML(html.replace(htmlReg, '').replace(commentReg, '')).trim()
}

export function sortedPosts (paths) {
  return paths
    .filter(p => !p.frontmatter.draft)
    .sort((a, b) => {
      // Use pubDate if available, otherwise fall back to date
      const dateA = a.frontmatter.pubDate || a.frontmatter.date
      const dateB = b.frontmatter.pubDate || b.frontmatter.date
      return new Date(dateB).valueOf() - new Date(dateA).valueOf()
    })
}
