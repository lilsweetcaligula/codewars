#include <string.h>
#include <stdlib.h>
#include <stdio.h>

static char *HTMLGenOpenClosingTag(const char *innerHTML, const char *openTag, const char *closeTag) {
  char *buffer = (char*)malloc(sizeof(char) * (1 + strlen(openTag) + strlen(innerHTML) + strlen(closeTag)));
  if (buffer) {
    (void)sprintf(buffer, "%s%s%s", openTag, innerHTML, closeTag);
  }
  return buffer;
}

static char *HTMLGenTag(const char *innerHTML, const char *tagName) {
  const size_t tagNameLength = strlen(tagName);
  
  // + 2: extra two chars for the opening tag: '<''>'
  char *openTag = (char*)malloc(sizeof(char) * (1 + tagNameLength + 2));
  
  if (!openTag) return NULL;
  
  // + 3: extra three chars for the closing tag: '<''/''>'
  char * closeTag = (char*)malloc(sizeof(char) * (1 + tagNameLength + 3));
  
  if (!closeTag) {
    free(openTag); openTag = NULL;
    return NULL;
  }
  
  (void)sprintf(openTag, "<%s>", tagName);
  (void)sprintf(closeTag, "</%s>", tagName);
  
  char *HTMLElement = HTMLGenOpenClosingTag(innerHTML, openTag, closeTag);
  
  free(openTag);   openTag  = NULL;
  free(closeTag);  closeTag = NULL;
  
  return HTMLElement;
}

char *HTMLGenA(const char *innerHTML) {
  return HTMLGenTag(innerHTML, "a");
}

char *HTMLGenB(const char *innerHTML) {
  return HTMLGenTag(innerHTML, "b");
}

char *HTMLGenBody(const char *innerHTML) {
  return HTMLGenTag(innerHTML, "body");
}

char *HTMLGenDiv(const char *innerHTML) {
  return HTMLGenTag(innerHTML, "div");
}

char *HTMLGenSpan(const char *innerHTML) {
  return HTMLGenTag(innerHTML, "span");
}

char *HTMLGenTitle(const char *innerHTML) {
  return HTMLGenTag(innerHTML, "title");
}

char *HTMLGenComment(const char *innerHTML) {
  return HTMLGenOpenClosingTag(innerHTML, "<!--", "-->");
}