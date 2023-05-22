<template>
  <div>
    <h5>작성한 댓글</h5>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <p>{{ comment.content }}</p>
        <!-- 댓글의 추가 필드들을 표시할 수 있음 -->
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'UserComment',
  data() {
    return {
      comments: [],
    };
  },
  props: {
    username : String,
  },
  created() {
    this.fetchUserComments();
  },
  methods: {
    fetchUserComments() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.username}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
      })
      .then(response => {
        this.comments = response.data;
      })
      .catch(error => {
        console.error(error);
      });
    },
  },
};
</script>

<style></style>
