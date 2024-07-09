<script setup lang="ts">
import { ref, onMounted } from "vue";
import {
  Sparkles,
  Book,
  Coffee,
  Feather,
  Code,
  Laptop,
  Users,
  MessageSquare,
} from "lucide-vue-next";
import { Button } from "@/components/ui/button";

const sections = ref([
  { id: "hero", visible: true },
  { id: "features", visible: false },
  { id: "articles", visible: false },
  { id: "about", visible: false },
]);

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const index = sections.value.findIndex((s) => s.id === entry.target.id);
        if (index !== -1) {
          sections.value[index].visible = entry.isIntersecting;
        }
      });
    },
    { threshold: 0.5 }
  );

  sections.value.forEach((section) => {
    const element = document.getElementById(section.id);
    if (element) observer.observe(element);
  });
});
</script>

<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <section
      id="hero"
      class="min-h-screen flex flex-col items-center justify-center bg-pastel-100 dark:bg-pastel-900 transition-all duration-1000 ease-in-out"
    >
      <Laptop class="w-24 h-24 text-pastel-500 mb-8 animate-fade-in-up" />
      <h1
        class="text-6xl font-bold mb-8 text-center text-pastel-800 dark:text-pastel-200 animate-fade-in-up animation-delay-300"
      >
        Welcome to My Static Site
      </h1>
      <p
        class="text-2xl mb-12 text-center text-pastel-600 dark:text-pastel-400 animate-fade-in-up animation-delay-600"
      >
        Discover a world of knowledge and inspiration
      </p>
      <Button class="animate-fade-in-up animation-delay-900" size="lg">
        Explore Articles
      </Button>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-pastel-200 dark:bg-pastel-800">
      <div class="container mx-auto px-4">
        <h2
          class="text-4xl font-bold mb-12 text-center text-pastel-800 dark:text-pastel-200"
          :class="{ 'animate-fade-in-up': sections[1].visible }"
        >
          Key Features
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            v-for="(feature, index) in [
              'Engaging Content',
              'Beautiful Design',
              'Easy Navigation',
            ]"
            :key="index"
            class="bg-pastel-100 dark:bg-pastel-700 p-6 rounded-lg shadow-lg transform transition-all duration-500 hover:scale-105"
            :class="{ 'animate-fade-in-up': sections[1].visible }"
            :style="{ animationDelay: `${index * 150}ms` }"
          >
            <div class="flex items-center justify-center mb-4">
              <component
                :is="index === 0 ? Sparkles : index === 1 ? Feather : Coffee"
                class="w-12 h-12 text-pastel-500"
              />
            </div>
            <h3
              class="text-xl font-semibold mb-2 text-center text-pastel-700 dark:text-pastel-300"
            >
              {{ feature }}
            </h3>
            <p class="text-pastel-600 dark:text-pastel-400 text-center">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Articles Preview Section -->
    <section id="articles" class="py-20 bg-pastel-300 dark:bg-pastel-700">
      <div class="container mx-auto px-4">
        <h2
          class="text-4xl font-bold mb-12 text-center text-pastel-800 dark:text-pastel-200"
          :class="{ 'animate-fade-in-up': sections[2].visible }"
        >
          Featured Articles
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="index in 3"
            :key="index"
            class="bg-pastel-100 dark:bg-pastel-600 p-6 rounded-lg shadow-lg transform transition-all duration-500 hover:scale-105"
            :class="{ 'animate-fade-in-up': sections[2].visible }"
            :style="{ animationDelay: `${index * 150}ms` }"
          >
            <Book class="w-12 h-12 text-pastel-500 mb-4 mx-auto" />
            <h3
              class="text-xl font-semibold mb-2 text-pastel-700 dark:text-pastel-300"
            >
              Article Title {{ index }}
            </h3>
            <p class="text-pastel-600 dark:text-pastel-400 mb-4">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus
              lacinia odio vitae vestibulum.
            </p>
            <Button variant="outline">Read More</Button>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-20 bg-pastel-400 dark:bg-pastel-600">
      <div class="container mx-auto px-4">
        <h2
          class="text-4xl font-bold mb-12 text-center text-pastel-800 dark:text-pastel-200"
          :class="{ 'animate-fade-in-up': sections[3].visible }"
        >
          About Us
        </h2>
        <div class="flex flex-col md:flex-row items-center justify-center">
          <div
            class="md:w-1/2 mb-8 md:mb-0 md:pr-8"
            :class="{ 'animate-fade-in-left': sections[3].visible }"
          >
            <Code
              class="w-24 h-24 text-pastel-700 dark:text-pastel-300 mx-auto mb-4"
            />
            <p class="text-lg text-pastel-700 dark:text-pastel-300 text-center">
              We're passionate about creating beautiful and informative content.
              Our goal is to inspire and educate through engaging articles and a
              delightful user experience.
            </p>
          </div>
          <div
            class="md:w-1/2 flex justify-center"
            :class="{ 'animate-fade-in-right': sections[3].visible }"
          >
            <div class="grid grid-cols-2 gap-4">
              <Users class="w-24 h-24 text-pastel-700 dark:text-pastel-300" />
              <MessageSquare
                class="w-24 h-24 text-pastel-700 dark:text-pastel-300"
              />
              <Laptop class="w-24 h-24 text-pastel-700 dark:text-pastel-300" />
              <Book class="w-24 h-24 text-pastel-700 dark:text-pastel-300" />
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.animate-fade-in-up {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-fade-in-left {
  opacity: 0;
  transform: translateX(-20px);
  animation: fadeInLeft 0.6s ease forwards;
}

.animate-fade-in-right {
  opacity: 0;
  transform: translateX(20px);
  animation: fadeInRight 0.6s ease forwards;
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInLeft {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animation-delay-300 {
  animation-delay: 300ms;
}

.animation-delay-600 {
  animation-delay: 600ms;
}

.animation-delay-900 {
  animation-delay: 900ms;
}
</style>
