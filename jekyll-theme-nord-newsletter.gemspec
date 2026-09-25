# frozen_string_literal: true

require_relative "lib/jekyll-theme-nord-newsletter/version"

Gem::Specification.new do |spec|
  spec.name          = "jekyll-theme-nord-newsletter"
  spec.version       = JekyllThemeNordNewsletter::VERSION
  spec.authors       = ["Palak Mathur"]
  spec.email         = ["palakmathur@gmail.com"]

  spec.summary       = "A Nord-palette Jekyll theme with a post grid, archives, tags, client-side search, a newsletter CTA, a command-line overlay, and light/dark theming."
  spec.description   = "Nord Newsletter is a config-driven Jekyll theme extracted from systemhalted.in: responsive post grid, archives/categories/tags, elasticlunr search overlay, a keyboard-driven command-line overlay, collection layouts, Giscus comments, and a configurable newsletter CTA — all configurable from _config.yml."
  spec.homepage      = "https://github.com/systemhalted/jekyll-theme-nord-newsletter"
  spec.license       = "MIT"
  spec.metadata      = {
    "plugin_type"       => "theme",
    "documentation_uri" => "https://rubydoc.info/gems/jekyll-theme-nord-newsletter",
    "source_code_uri"   => "https://github.com/systemhalted/jekyll-theme-nord-newsletter",
    "changelog_uri"     => "https://github.com/systemhalted/jekyll-theme-nord-newsletter/blob/main/CHANGELOG.md"
  }
  spec.required_ruby_version = ">= 2.7"

  spec.files = Dir.glob("{assets,_includes,_layouts,_sass,_data,lib}/**/*", File::FNM_DOTMATCH)
                  .select { |f| File.file?(f) } +
               %w[CHANGELOG.md LICENSE.md README.md]

  spec.add_runtime_dependency "jekyll", "~> 4.3"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.15"
  spec.add_runtime_dependency "jekyll-paginate", "~> 1.1"
  spec.add_runtime_dependency "jekyll-gist", "~> 1.5"
  spec.add_runtime_dependency "jekyll-sitemap", "~> 1.4"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.8"
  spec.add_runtime_dependency "jekyll-toc", "~> 0.18"

  spec.require_paths = ["lib"]
end
