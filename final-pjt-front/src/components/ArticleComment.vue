<template>
  <div>
    <h3>댓글 창</h3>
    <template v-if="comments.length">
      <ArticleCommentItem v-for="comment in comments" :key="comment.id" :comment="comment" />
    </template>
    <template v-else>
      <p>댓글이 아직 아무것도 없습니다.</p>
    </template>
    <form @submit.prevent="addComment">
      <label for="content">댓글 작성</label>
      <textarea id="content" v-model="newCommentContent"></textarea><br>
      <button type="submit">댓글 추가</button>
    </form>
  </div>
</template>

<script>
import ArticleCommentItem from '@/components/ArticleCommentItem'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleComment',
  components: {
    ArticleCommentItem,
  },
  props: {
    comments: {
      type: Array,
      default: () => [],
    },
    articleId : String,
    },
  data() {
    return {
      newCommentContent: '',
      localComments: [],
    }
  },
  created() {
    this.localComments = this.comments
  },
  methods: {
    addComment() {
      const content = this.newCommentContent.trim();
      if (!content) {
        alert('댓글 내용을 입력해주세요.');
        return;
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/${this.articleId}/comments/create`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
        data: {
          content: this.newCommentContent,
        }
      })
        .then((res) => {
          const newComment = res.data
          this.localComments.push(newComment)
          this.newCommentContent = ''
          location.reload();
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style></style>
