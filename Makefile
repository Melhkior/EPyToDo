#
## EPITECH PROJECT, 2017
## Makefile
## File description:
## Makefile
##

SRC	=	sources/xxx.c	\

OBJ	=	$(SRC:%.c=%.o)

NAME	=	xxx

INC	=	-I./include

INC_LIB = 	-I./lib/my/include

LIBS	=	-L./lib/my -lmy

CFLAGS	=	$(INC) $(INC_LIB) -Wextra -Wall -Werror

CC	=	gcc

LIB	=	$(MAKE) -C lib/my/

all:		$(NAME)

$(NAME):	$(OBJ)
		$(LIB)
		$(CC) -o $(NAME) $(OBJ) $(LIBS)

clean:
		$(RM) -f $(OBJ)
		$(MAKE) clean -C lib/my/

fclean: 	clean
		$(RM) -f $(NAME)
		$(MAKE) fclean -C lib/my/

re:		fclean all
