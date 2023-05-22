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
        <p>{{ formatDateTime(article.created_at) }}</p>
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
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
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
