<script setup lang="ts">
import { ref, onMounted, watch, computed } from "vue";
import { useRoute } from "vue-router";
import MarkdownIt from "markdown-it";
import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";
import "highlight.js/styles/atom-one-light.css";
import ArticleHeader from "@/components/ArticleHeader.vue";
import ArticleContent from "@/components/ArticleContent.vue";
import ThemeToggle from "@/components/ThemeToggle.vue";
import ColorPaletteSelector from "@/components/ColorPaletteSelector.vue";

const route = useRoute();
const content = ref("");
const title = ref("");
const date = ref("");
const isLoading = ref(true);
const isDarkTheme = ref(false);
const selectedPalette = ref({
  name: "Pastel Rainbow",
  value: "pastel-rainbow",
});

const md = new MarkdownIt({
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return hljs.highlight(str, { language: lang }).value;
      } catch (__) {}
    }
    return ""; // use external default escaping
  },
});

const toggleTheme = () => {
  isDarkTheme.value = !isDarkTheme.value;
};

const fetchArticle = async () => {
  isLoading.value = true;
  try {
    const contentResponse = await fetch(
      `${import.meta.env.BASE_URL}/content/${route.params.slug}.md`
    );
    const markdown = await contentResponse.text();
    content.value = md.render(markdown);

    const metadataResponse = await fetch(
      `${import.meta.env.BASE_URL}/articles.json`
    );
    const articles = await metadataResponse.json();
    const currentArticle = articles.find(
      (article: any) => article.slug === route.params.slug
    );
    if (currentArticle) {
      title.value = currentArticle.title;
      date.value = new Date(currentArticle.date).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    }
  } catch (error) {
    console.error("Failed to fetch article:", error);
    content.value = "<p>Failed to load article.</p>";
  } finally {
    isLoading.value = false;
  }
};

onMounted(fetchArticle);

watch(
  () => route.params.slug,
  (newSlug) => {
    if (newSlug) {
      fetchArticle();
    }
  }
);

const themeClasses = computed(() => {
  return isDarkTheme.value
    ? "bg-gray-900 text-white"
    : "bg-white text-gray-900";
});

const codeThemeClasses = computed(() => {
  return isDarkTheme.value ? "hljs-atom-one-dark" : "hljs-atom-one-light";
});

const paletteClasses = computed(() => {
  const baseClasses = "transition-colors duration-300";
  const lightClasses = {
    "pastel-rainbow":
      "bg-gradient-to-r from-pink-100 via-purple-100 to-indigo-100",
    "ocean-breeze": "bg-gradient-to-r from-cyan-100 via-blue-100 to-teal-100",
    "spring-bloom":
      "bg-gradient-to-r from-green-100 via-yellow-100 to-pink-100",
    "sunset-glow": "bg-gradient-to-r from-orange-100 via-red-100 to-purple-100",
    "forest-mist": "bg-gradient-to-r from-emerald-100 via-teal-100 to-cyan-100",
  };
  const darkClasses = {
    "pastel-rainbow":
      "dark:bg-gradient-to-r dark:from-pink-900 dark:via-purple-900 dark:to-indigo-900",
    "ocean-breeze":
      "dark:bg-gradient-to-r dark:from-cyan-900 dark:via-blue-900 dark:to-teal-900",
    "spring-bloom":
      "dark:bg-gradient-to-r dark:from-green-900 dark:via-yellow-900 dark:to-pink-900",
    "sunset-glow":
      "dark:bg-gradient-to-r dark:from-orange-900 dark:via-red-900 dark:to-purple-900",
    "forest-mist":
      "dark:bg-gradient-to-r dark:from-emerald-900 dark:via-teal-900 dark:to-cyan-900",
  };

  //@ts-ignore
  return `${baseClasses} ${lightClasses[selectedPalette.value.value]} ${
    //@ts-ignore
    darkClasses[selectedPalette.value.value]
  }`;
});
</script>

<template>
  <article
    :class="[
      'max-w-3xl mx-auto px-4 py-8 transition-colors duration-300 rounded-2xl',
      paletteClasses,
    ]"
  >
    <div class="flex justify-between items-center mb-8">
      <ArticleHeader :title="title" :date="date" :isLoading="isLoading" />
      <div class="flex items-center space-x-4">
        <ColorPaletteSelector @select="selectedPalette = $event" />
        <ThemeToggle :isDarkTheme="isDarkTheme" @toggle="toggleTheme" />
      </div>
    </div>

    <ArticleContent
      :content="content"
      :isLoading="isLoading"
      :codeThemeClasses="codeThemeClasses"
    />
  </article>
</template>

<style>
@import "highlight.js/styles/atom-one-dark.css";
@import "highlight.js/styles/atom-one-light.css";

.prose {
  @apply text-lg leading-relaxed;
}

.prose h1,
.prose h2,
.prose h3,
.prose h4,
.prose h5,
.prose h6 {
  @apply font-bold my-4;
}

.prose h1 {
  @apply text-3xl;
}

.prose h2 {
  @apply text-2xl;
}

.prose h3 {
  @apply text-xl;
}

.prose p {
  @apply my-4;
}

.prose ul,
.prose ol {
  @apply my-4 ml-6;
}

.prose li {
  @apply my-2;
}

.prose a {
  @apply text-blue-500 hover:text-blue-600 underline;
}

.prose code {
  @apply px-1 py-0.5 rounded text-sm;
}

.prose pre {
  @apply p-4 rounded-lg overflow-x-auto;
}

.prose blockquote {
  @apply border-l-4 border-gray-300 dark:border-gray-700 pl-4 italic my-4;
}

.hljs-atom-one-dark .hljs {
  @apply bg-gray-800;
}

.hljs-atom-one-light .hljs {
  @apply bg-gray-100;
}
</style>
