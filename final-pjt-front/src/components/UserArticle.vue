<template>
  <div>
    <h5>작성한 글</h5>
    <ul>
      <li v-for="article in articles" :key="article.id">
          <router-link :to="{
          name: 'ArticleDetailView',
          params: {id: article.id }}">
          <h6>{{ article.title }}</h6>
        </router-link>
        <p>{{ article.created_at }}</p>
        <!-- 게시물의 이미지 등 다른 필드들을 표시할 수 있음 -->
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'UserArticle',
  data() {
    return {
      articles: [],
    };
  },
  props: {
    username : String,
  },
  created() {
    this.fetchUserArticles();
  },
  methods: {
    fetchUserArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.username}/articles/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
      })
      .then(response => {
        this.articles = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  },
};
</script>

<style></style>
