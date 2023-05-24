<template>
  <div class="comment-color">
    <template v-if="comments.length">
      <ArticleCommentItem v-for="comment in comments" :key="comment.id" :comment="comment" />
    </template>
    <template v-else>
      <p>댓글이 아직 아무것도 없습니다.</p>
    </template>
    <form @submit.prevent="addComment">
      <textarea id="content" v-model="newCommentContent"  class="form-control" rows="1" placeholder="댓글을 입력하세요"></textarea><br>
      <button type="submit" class="btn btn-primary mb-4">댓글 작성</button>
    </form>
  </div>
</template>

<script>
import ArticleCommentItem from '@/components/ArticleCommentItem'
import axios from 'axios'

const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'ArticleComment',
  components: {
    ArticleCommentItem,
  },
  props: {
    articleId : Number,
    },
  data() {
    return {
      newCommentContent: '',
      comments: [],
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getComment()
    this.$eventBus.$on('commentDeleted', () => {
      this.getComment();
    });
  },
  methods: {
    getComment(){
      axios({
          method: 'get',
          url: `${API_URL}/articles/${ this.articleId }/comments/`,
          headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
          },
        })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    addComment() {
      if(this.isLogin){
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
        this.comments.push(newComment)
        this.newCommentContent = ''
        this.getComment
      })
      .catch((err) => {
        console.log(err)
      })
      } else {
          alert('로그인한 유저만 댓글을 작성할 수 있습니다.')
          this.$router.push('/login')
      }
    }
  },
}
</script>

<style scoped>
.btn-primary {
  background-color: #4f3d63;
  border-color: #4f3d63;
}

.btn-primary:hover {
  background-color: #7c6891;
  border-color: #7c6891;
}

.comment-color {
  border-color: #bfbfbf;
}


</style>
