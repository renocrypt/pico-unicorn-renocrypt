import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Article from '@/components/Article.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/article/:path', name: 'Article', component: Article },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router