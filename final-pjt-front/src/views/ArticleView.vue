<template>
  <div>
    <h2 class="title-mg-ct">Community</h2>
    <div v-if="isLogin" class="go-article-page">
      <router-link :to="{ name: 'ArticleCreateView' }" class="btn btn-article-view">새 글쓰기</router-link>
    </div>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')     
    }
  }
}
</script>

<style>
.btn-article-view {
  background-color: #261639;
  border-color: #261639;
  color: #bfbfbf;
}

.btn-article-view:hover {
  background-color: #7c6891;
  border-color: #7c6891;
}

.go-article-page {
  margin-top: 10px; 
}

</style>
